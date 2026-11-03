import allure

from locators.locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    """Страница ленты заказов"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderFeedPageLocators()

    @allure.step("Нажать на первый заказ в ленте")
    def click_first_order(self):
        self.click_element(self.locators.ORDER_LINK)

    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        self.click_element(self.locators.ORDER_MODAL_CLOSE)

    @allure.step("Проверить, что модалка заказа открыта")
    def is_order_modal_open(self):
        return self.count_elements(self.locators.ORDER_MODAL) > 0

    @allure.step("Получить счётчик 'Выполнено за все время'")
    def get_total_orders_count(self):
        element = self.wait_for_element_visible(self.locators.TOTAL_ORDERS_COUNTER)
        return int(element.text)

    @allure.step("Получить счётчик 'Выполнено за сегодня'")
    def get_today_orders_count(self):
        element = self.wait_for_element_visible(self.locators.TODAY_ORDERS_COUNTER)
        return int(element.text)

    @allure.step("Дождаться увеличения счётчика 'Выполнено за сегодня'")
    def wait_today_orders_count_increase(self, previous_value, timeout=15):
        self.wait_until(
            lambda d: int(d.find_element(*self.locators.TODAY_ORDERS_COUNTER).text) > previous_value,
            timeout
        )

    @allure.step("Получить количество заказов 'В работе'")
    def get_orders_in_progress_count(self):
        return self.count_elements(self.locators.ORDERS_IN_PROGRESS)

    @allure.step("Проверить, что заказ отображается в ленте")
    def is_order_in_feed(self, order_number, timeout=20):
        self.refresh_page()
        try:
            self.wait_until(
                lambda d: any(
                    order_number in el.text.replace("#", "")
                    for el in d.find_elements(*self.locators.ORDER_ITEM)
                ),
                timeout
            )
            return True
        except Exception:
            return False