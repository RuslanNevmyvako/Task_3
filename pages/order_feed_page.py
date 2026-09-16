import allure
from pages.base_page import BasePage
from locators.locators import OrderFeedPageLocators
from selenium.webdriver.support import expected_conditions as EC


class OrderFeedPage(BasePage):
    """Страница ленты заказов"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderFeedPageLocators()

    @allure.step("Нажать на первый заказ в ленте")
    def click_first_order(self):
        element = self.wait_for_element_visible(self.locators.ORDER_LINK)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        close_btn = self.wait_for_element_visible(self.locators.ORDER_MODAL_CLOSE)
        self.driver.execute_script("arguments[0].click();", close_btn)

    @allure.step("Проверить, что модалка заказа открыта")
    def is_order_modal_open(self):
        elements = self.driver.find_elements(*self.locators.ORDER_MODAL)
        return len(elements) > 0

    @allure.step("Получить счётчик 'Выполнено за все время'")
    def get_total_orders_count(self):
        element = self.wait_for_element_visible(self.locators.TOTAL_ORDERS_COUNTER)
        return int(element.text)

    @allure.step("Получить счётчик 'Выполнено за сегодня'")
    def get_today_orders_count(self):
        element = self.wait_for_element_visible(self.locators.TODAY_ORDERS_COUNTER)
        return int(element.text)

    @allure.step("Дождаться, что счётчик 'Выполнено за сегодня' увеличится")
    def wait_today_orders_count_increase(self, previous_value, timeout=15):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.common.exceptions import TimeoutException

        def check(d):
            try:
                current = int(d.find_element(*self.locators.TODAY_ORDERS_COUNTER).text)
                return current > previous_value
            except Exception:
                return False

        WebDriverWait(self.driver, timeout).until(check)

    @allure.step("Получить количество заказов 'В работе'")
    def get_orders_in_progress_count(self):
        orders = self.driver.find_elements(*self.locators.ORDERS_IN_PROGRESS)
        return len(orders)

    @allure.step("Проверить, что заказ отображается в ленте")
    def is_order_in_feed(self, order_number):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.common.exceptions import TimeoutException

        self.driver.refresh()

        def check(d):
            try:
                elements = d.find_elements(*self.locators.ORDER_ITEM)
                return any(order_number in el.text.replace("#", "") for el in elements)
            except Exception:
                return False

        try:
            WebDriverWait(self.driver, 20).until(check)
            return True
        except TimeoutException:
            return False