import allure

from locators.locators import ProfilePageLocators
from pages.base_page import BasePage


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

    @allure.step("Нажать на 'Выход'")
    def click_logout(self):
        self.click_element(self.locators.LOGOUT_BUTTON)
        self.wait_for_url("login")

    @allure.step("Проверить наличие заказов в истории")
    def has_orders_in_history(self):
        return self.count_elements(self.locators.ORDER_IN_HISTORY) > 0

    @allure.step("Получить номера заказов из истории")
    def get_order_numbers_from_history(self):
        self.wait_for_element_visible(self.locators.ORDER_IN_HISTORY)
        orders = self.find_elements(self.locators.ORDER_IN_HISTORY)
        numbers = []
        for order in orders:
            number_el = order.find_element(*self.locators.ORDER_NUMBER_IN_HISTORY)
            numbers.append(number_el.text.replace("#", ""))
        return numbers