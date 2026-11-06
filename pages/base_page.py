from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def open_url(self, url):
        """Открыть URL в браузере"""
        self.driver.get(url)

    def refresh_page(self):
        """Обновить страницу"""
        self.driver.refresh()

    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url

    def wait_for_url(self, expected_url):
        """Ждать, пока URL содержит строку"""
        return self.wait.until(EC.url_contains(expected_url))

    def wait_for_url_not_contains(self, substring):
        """Ждать, пока URL НЕ содержит строку"""
        return self.wait.until(lambda d: substring not in d.current_url)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element(self, locator, timeout=30):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        element = self.wait_for_element_visible(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def is_element_displayed(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except Exception:
            return False

    def find_elements(self, locator):
        """Найти все элементы по локатору (без ожидания)"""
        return self.driver.find_elements(*locator)

    def count_elements(self, locator):
        """Количество элементов по локатору"""
        return len(self.find_elements(locator))

    def execute_script(self, script, *args):
        """Выполнить JS-скрипт"""
        return self.driver.execute_script(script, *args)

    def wait_until(self, condition, timeout=30):
        """Универсальное ожидание условия"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(condition)

    def drag_and_drop(self, source_locator, target_locator):
        """
        Drag-n-drop с учётом браузера.
        Chrome: ActionChains работает напрямую.
        Firefox: geckodriver не отдаёт события dragstart/drop для React —
        используем JS-эмуляцию событий.
        """
        source = self.wait_for_element_visible(source_locator)
        target = self.wait.until(EC.presence_of_element_located(target_locator))

        browser = self.driver.capabilities.get("browserName", "").lower()

        if browser == "firefox":
            js = """
            function createEvent(type, dataTransfer) {
                var event = document.createEvent('CustomEvent');
                event.initCustomEvent(type, true, true, null);
                event.dataTransfer = dataTransfer;
                return event;
            }
            function createDataTransfer() {
                var data = {};
                return {
                    data: data,
                    setData: function(k, v) { this.data[k] = v; },
                    getData: function(k) { return this.data[k]; },
                    dropEffect: 'move',
                    effectAllowed: 'all'
                };
            }
            var dt = createDataTransfer();
            arguments[0].dispatchEvent(createEvent('dragstart', dt));
            arguments[0].dispatchEvent(createEvent('drag', dt));
            arguments[1].dispatchEvent(createEvent('dragenter', dt));
            arguments[1].dispatchEvent(createEvent('dragover', dt));
            arguments[1].dispatchEvent(createEvent('drop', dt));
            arguments[0].dispatchEvent(createEvent('dragend', dt));
            """
            self.driver.execute_script(js, source, target)
        else:
            ActionChains(self.driver) \
                .move_to_element(source) \
                .click_and_hold() \
                .pause(0.5) \
                .move_to_element(target) \
                .pause(0.5) \
                .release() \
                .perform()