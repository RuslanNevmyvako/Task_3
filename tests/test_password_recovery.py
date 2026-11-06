import allure

from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:
    """Тесты для восстановления пароля"""

    @allure.title("Переход на страницу восстановления пароля по кнопке 'Восстановить пароль'")
    def test_go_to_password_recovery_page(self, driver):
        login_page = LoginPage(driver)
        login_page.click_forgot_password_link()
        login_page.wait_for_url("forgot-password")

        assert "forgot-password" in login_page.get_current_url(), \
            f"Не произошел переход. Текущий URL: {login_page.get_current_url()}"

    @allure.title("Ввод почты и клик по кнопке 'Восстановить'")
    def test_restore_password(self, driver, create_user_via_api):
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        user_data = create_user_via_api["data"]

        login_page.click_forgot_password_link()
        login_page.wait_for_url("forgot-password")
        forgot_password_page.enter_email(user_data["email"])
        forgot_password_page.click_restore_button()
        forgot_password_page.wait_for_url("forgot-password")

        assert "forgot-password" in forgot_password_page.get_current_url(), \
            f"Клик по 'Восстановить' привел к ошибке. Текущий URL: {forgot_password_page.get_current_url()}"

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_show_password_button_highlights_field(self, driver):
        """
        Проверяем на странице логина: /reset-password без токена из письма
        редиректит на /forgot-password, а компонент поля пароля с иконкой
        показа тот же, что и на /reset-password.
        """
        login_page = LoginPage(driver)
        login_page.go_to_login_page()
        login_page.enter_password("TestPassword123!")
        login_page.click_show_password_button()

        assert login_page.is_password_field_active(), \
            "Поле пароля не стало активным (пароль не показан)"