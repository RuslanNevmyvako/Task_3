import pytest
import allure
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:
    """Тесты для восстановления пароля"""
    
    @allure.title("Переход на страницу восстановления пароля по кнопке 'Восстановить пароль'")
    def test_go_to_password_recovery_page(self, driver):
        """Проверка перехода на страницу восстановления пароля"""
        login_page = LoginPage(driver)
        login_page.click_forgot_password_link()
        current_url = login_page.get_current_url()
        assert "forgot-password" in current_url, f"Не произошел переход. Текущий URL: {current_url}"
    
    @allure.title("Ввод почты и клик по кнопке 'Восстановить'")
    def test_restore_password(self, driver, create_user_via_api):
        """Проверка ввода почты и клика по кнопке восстановления"""
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        
        # Используем email реального пользователя
        user_data = create_user_via_api["data"]
        
        # Переходим на страницу восстановления
        login_page.click_forgot_password_link()
        
        # Вводим email и нажимаем восстановить
        forgot_password_page.enter_email(user_data["email"])
        forgot_password_page.click_restore_button()
        
        # Ждём редирект на страницу сброса пароля
        forgot_password_page.wait_for_url("reset-password")
        
        # Проверяем переход на страницу сброса пароля
        current_url = forgot_password_page.get_current_url()
        assert "reset-password" in current_url, f"Не произошел переход. Текущий URL: {current_url}"
    
    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_show_password_button_highlights_field(self, driver, create_user_via_api):
        """Проверка, что кнопка показа пароля подсвечивает поле"""
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)
        
        user_data = create_user_via_api["data"]
        
        # Переходим на страницу восстановления
        login_page.click_forgot_password_link()
        
        # Вводим реальный email и нажимаем восстановить
        forgot_password_page.enter_email(user_data["email"])
        forgot_password_page.click_restore_button()
        
        # Ждём перехода на страницу сброса пароля
        forgot_password_page.wait_for_url("reset-password")
        
        # Кликаем показать пароль
        reset_password_page.click_show_password_button()
        
        # Проверяем, что поле пароля в фокусе (подсвечено)
        is_active = reset_password_page.is_password_field_active()
        assert is_active, "Поле пароля не стало активным после клика на кнопку показа"