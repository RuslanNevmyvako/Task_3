import time
import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.feature("Личный кабинет")
class TestProfile:
    """Тесты для личного кабинета"""
    
    @allure.title("Переход по клику на 'Личный кабинет'")
    def test_go_to_profile(self, driver, create_user_via_api):
        """Проверка перехода в личный кабинет"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        # Авторизуемся
        user_data = create_user_via_api["data"]
        login_page.login(user_data["email"], user_data["password"])

        # Кликаем на "Личный кабинет"
        main_page.click_profile()

        # Проверяем переход в личный кабинет
        current_url = profile_page.get_current_url()
        assert "account" in current_url, f"Не произошел переход в личный кабинет. Текущий URL: {current_url}"
    
    @allure.title("Переход в раздел 'История заказов'")
    def test_go_to_order_history(self, driver, create_user_via_api):
        """Проверка перехода в раздел 'История заказов'"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        user_data = create_user_via_api["data"]
        login_page.login(user_data["email"], user_data["password"])

        main_page.click_profile()
        profile_page.click_order_history()
        profile_page.wait_for_url("order-history")

        current_url = profile_page.get_current_url()
        assert "order-history" in current_url, f"Не произошел переход. Текущий URL: {current_url}"
            
    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, create_user_via_api):
        """Проверка выхода из аккаунта"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)
        
        # Авторизуемся
        user_data = create_user_via_api["data"]
        login_page.login(user_data["email"], user_data["password"])
        
        # Переходим в профиль
        main_page.click_profile()
        
        profile_page.click_logout()
        
        # Проверяем результат
        current_url = profile_page.get_current_url()
        assert "login" in current_url, f"Не произошел выход. Текущий URL: {current_url}"