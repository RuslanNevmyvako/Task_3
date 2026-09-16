import allure
from pages.base_page import BasePage
from locators.locators import MainPageLocators


class MainPage(BasePage):
    """Главная страница"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step("Нажать на 'Конструктор'")
    def click_constructor(self):
        element = self.wait_for_element_visible(self.locators.CONSTRUCTOR_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Нажать на 'Лента заказов'")
    def click_order_feed(self):
        element = self.wait_for_element_visible(self.locators.ORDER_FEED_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Нажать на 'Личный кабинет'")
    def click_profile(self):
        element = self.wait_for_element_visible(self.locators.PROFILE_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Кликнуть на булочку (открывает модалку)")
    def click_first_ingredient(self):
        element = self.wait_for_element_visible(self.locators.BUN_INGREDIENT)
        self.driver.execute_script("arguments[0].click();", element)
        self.wait_for_element_visible(self.locators.INGREDIENT_MODAL)

    @allure.step("Добавить булочку в заказ")
    def add_bun_to_order(self):
        self.drag_and_drop(
            self.locators.BUN_INGREDIENT,
            self.locators.BUN_TOP_DROP_ZONE
        )

    @allure.step("Добавить соус в заказ")
    def add_sauce_to_order(self):
        self.drag_and_drop(
            self.locators.SAUCE_INGREDIENT,
            self.locators.BASKET_LIST
        )

    @allure.step("Закрыть модальное окно")
    def close_ingredient_modal(self):
        close_btn = self.wait_for_element_visible(self.locators.INGREDIENT_MODAL_CLOSE)
        self.driver.execute_script("arguments[0].click();", close_btn)

    @allure.step("Проверить, что модальное окно открыто")
    def is_ingredient_modal_open(self):
        elements = self.driver.find_elements(*self.locators.INGREDIENT_MODAL)
        return len(elements) > 0

    @allure.step("Проверить, что модальное окно закрыто")
    def is_ingredient_modal_closed(self):
        elements = self.driver.find_elements(*self.locators.INGREDIENT_MODAL)
        return len(elements) == 0

    @allure.step("Получить счётчик ингредиента")
    def get_ingredient_counter(self, ingredient_type="bun"):
        if ingredient_type == "bun":
            locator = self.locators.BUN_INGREDIENT
        elif ingredient_type == "sauce":
            locator = self.locators.SAUCE_INGREDIENT
        else:
            locator = self.locators.FILLING_INGREDIENT

        element = self.find_element(locator)
        counter = element.find_element(*self.locators.INGREDIENT_COUNTER)
        return int(counter.text)

    @allure.step("Нажать кнопку 'Оформить заказ'")
    def click_place_order(self):
        element = self.wait_for_element_visible(self.locators.PLACE_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)
        self.wait_for_element_visible(self.locators.ORDER_NUMBER_MODAL)

    @allure.step("Закрыть модалку с номером заказа")
    def close_order_modal(self):
        close_btn = self.wait_for_element_visible(self.locators.ORDER_NUMBER_MODAL_CLOSE)
        self.driver.execute_script("arguments[0].click();", close_btn) 

    @allure.step("Проверить, что модалка с номером заказа открыта")
    def is_order_modal_open(self):
        return self.is_element_displayed(self.locators.ORDER_NUMBER_MODAL)

    @allure.step("Получить номер заказа из модалки")
    def get_order_number(self):
        element = self.wait_for_element_visible(self.locators.ORDER_NUMBER)
        return element.text