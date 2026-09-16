import pytest
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from pages.profile_page import ProfilePage


@allure.feature("Лента заказов")
class TestOrderFeed:
    """Тесты для ленты заказов"""

    @allure.title("Клик на заказ - открывается всплывающее окно с деталями")
    def test_order_click_shows_modal(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.click_order_feed()
        order_feed_page.click_first_order()

        assert order_feed_page.is_order_modal_open(), "Модальное окно с деталями заказа не открылось"

    @allure.title("Заказы пользователя из 'Истории заказов' отображаются в 'Ленте заказов'")
    def test_orders_from_history_visible_in_feed(self, driver, create_user_via_api, create_order_via_api):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)
        order_feed_page = OrderFeedPage(driver)

        user_data = create_user_via_api["data"]
        login_page.login(user_data["email"], user_data["password"])

        main_page.click_profile()
        profile_page.click_order_history()

        order_numbers = profile_page.get_order_numbers_from_history()
        assert len(order_numbers) > 0, "Нет заказов в истории"

        main_page.click_order_feed()
        order_feed_page.wait_for_url("feed")
        assert order_feed_page.is_order_in_feed(order_numbers[0]), \
            f"Заказ {order_numbers[0]} не отображается в ленте"

    @allure.title("При создании нового заказа счетчик 'Выполнено за все время' увеличивается")
    def test_total_orders_counter_increases(self, driver, create_user_via_api):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)

        user_data = create_user_via_api["data"]
        login_page.login(user_data["email"], user_data["password"])

        main_page.click_order_feed()
        order_feed_page.wait_for_url("feed")
        initial_count = order_feed_page.get_total_orders_count()

        main_page.click_constructor()
        main_page.add_bun_to_order()
        main_page.add_sauce_to_order()
        main_page.click_place_order()
        main_page.close_order_modal()

        main_page.click_order_feed()
        order_feed_page.wait_for_url("feed")
        new_count = order_feed_page.get_total_orders_count()

        assert new_count > initial_count, \
            f"Счетчик не увеличился. Было: {initial_count}, стало: {new_count}"


    @allure.title("При создании нового заказа счетчик 'Выполнено за сегодня' увеличивается")
    def test_today_orders_counter_increases(self, driver, create_user_via_api):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)

        user_data = create_user_via_api["data"]
        login_page.login(user_data["email"], user_data["password"])

        main_page.click_order_feed()
        order_feed_page.wait_for_url("feed")
        initial_count = order_feed_page.get_today_orders_count()

        main_page.click_constructor()
        main_page.add_bun_to_order()
        main_page.add_sauce_to_order()
        main_page.click_place_order()
        main_page.close_order_modal()

        main_page.click_order_feed()
        order_feed_page.wait_for_url("feed")
        order_feed_page.wait_today_orders_count_increase(initial_count)
        new_count = order_feed_page.get_today_orders_count()

        assert new_count > initial_count, \
            f"Счетчик не увеличился. Было: {initial_count}, стало: {new_count}"
            

    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_order_number_appears_in_progress(self, driver, create_user_via_api, create_order_via_api):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)

        order_number = str(create_order_via_api["order"]["number"])

        user_data = create_user_via_api["data"]
        login_page.login(user_data["email"], user_data["password"])

        main_page.click_order_feed()
        order_feed_page.wait_for_url("feed")

        assert order_feed_page.is_order_in_feed(order_number), \
            f"Заказ {order_number} не появился в ленте"