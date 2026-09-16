import allure
from pages.base_page import BasePage
from locators.locators import ProfilePageLocators


class ProfilePage(BasePage):
    """Страница личного кабинета"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProfilePageLocators()
    
    @allure.step("Нажать на 'Профиль'")
    def click_profile(self):
        self.click_element(self.locators.PROFILE_LINK)
    
    @allure.step("Нажать на 'История заказов'")
    def click_order_history(self):
        self.click_element(self.locators.ORDER_HISTORY_LINK)
        self.wait_for_url("order-history")
    
    @allure.step("Нажать на 'Выход'")
    def click_logout(self):
        """Клик на 'Выход' с ожиданием редиректа на страницу входа"""
        element = self.wait_for_element_visible(self.locators.LOGOUT_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)
        # Ждём редирект прямо здесь — тест остаётся чистым
        self.wait_for_url("login")

    @allure.step("Проверить наличие заказов в истории")
    def has_orders_in_history(self):
        try:
            orders = self.driver.find_elements(*self.locators.ORDER_IN_HISTORY)
            return len(orders) > 0
        except:
            return False
    
    @allure.step("Получить заказы из истории")
    def get_order_numbers_from_history(self):
        # Ждём пока список заказов появится в DOM
        self.wait_for_element_visible(self.locators.ORDER_IN_HISTORY)
        orders = self.driver.find_elements(*self.locators.ORDER_IN_HISTORY)
        numbers = []
        for order in orders:
            number_el = order.find_element(*self.locators.ORDER_NUMBER_IN_HISTORY)
            numbers.append(number_el.text.replace("#", ""))
        return numbers