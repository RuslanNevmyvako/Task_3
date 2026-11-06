import allure

from data import BASE_URL
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.feature("Основной функционал")
class TestMainFunctionality:
    """Тесты для основного функционала"""

    @allure.title("Переход по клику на 'Конструктор'")
    def test_go_to_constructor(self, driver):
        """Переход в конструктор"""
        main_page = MainPage(driver)
        main_page.click_order_feed()
        main_page.click_constructor()

        current_url = main_page.get_current_url()
        assert BASE_URL in current_url, f"Не произошел переход в конструктор. Текущий URL: {current_url}"

    @allure.title("Переход по клику на 'Лента заказов'")
    def test_go_to_order_feed(self, driver):
        """Переход в ленту заказов"""
        main_page = MainPage(driver)
        main_page.click_order_feed()

        current_url = main_page.get_current_url()
        assert "feed" in current_url, f"Не произошел переход в ленту заказов. Текущий URL: {current_url}"

    @allure.title("Клик на ингредиент - появляется всплывающее окно с деталями")
    def test_ingredient_click_shows_modal(self, driver):
        """Клик на ингредиент открывает модальное окно"""
        main_page = MainPage(driver)
        main_page.click_first_ingredient()

        assert main_page.is_ingredient_modal_open(), "Модальное окно не открылось"

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_modal_closes_by_cross(self, driver):
        """Клик по крестику закрывает модальное окно"""
        main_page = MainPage(driver)
        main_page.click_first_ingredient()
        main_page.close_ingredient_modal()

        assert main_page.is_ingredient_modal_closed(), "Модальное окно не закрылось"

    @allure.title("При добавлении ингредиента в заказ увеличивается каунтер")
    def test_ingredient_counter_increases(self, driver):
        """Добавление ингредиента увеличивает счётчик"""
        main_page = MainPage(driver)
        initial_counter = main_page.get_ingredient_counter("bun")
        main_page.add_bun_to_order()
        new_counter = main_page.get_ingredient_counter("bun")

        assert new_counter > initial_counter, \
            f"Счетчик не увеличился. Было: {initial_counter}, стало: {new_counter}"

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_authorized_user_can_create_order(self, driver, create_user_via_api):
        """Оформление заказа авторизованным пользователем"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        user_data = create_user_via_api["data"]
        login_page.login(user_data["email"], user_data["password"])

        main_page.add_bun_to_order()
        main_page.add_sauce_to_order()
        main_page.click_place_order()

        assert main_page.is_order_modal_open(), "Модальное окно с номером заказа не открылось"