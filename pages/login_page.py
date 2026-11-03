import allure

from data import LOGIN_URL
from locators.locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Страница входа"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators()

    @allure.step("Перейти на страницу входа")
    def go_to_login_page(self):
        self.open_url(LOGIN_URL)
        self.wait_for_element_visible(self.locators.EMAIL_INPUT)

    @allure.step("Ввести email")
    def enter_email(self, email):
        element = self.wait_for_element_visible(self.locators.EMAIL_INPUT)
        element.clear()
        element.send_keys(email)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        element = self.wait_for_element_visible(self.locators.PASSWORD_INPUT)
        element.clear()
        element.send_keys(password)

    @allure.step("Нажать кнопку показать/скрыть пароль")
    def click_show_password_button(self):
        self.click_element(self.locators.SHOW_PASSWORD_BUTTON)

    @allure.step("Проверить, что поле пароля активно (пароль показан)")
    def is_password_field_active(self):
        element = self.find_element(self.locators.PASSWORD_INPUT)
        return element.get_attribute("type") == "text"

    @allure.step("Нажать кнопку 'Войти'")
    def click_login_button(self):
        self.click_element(self.locators.LOGIN_BUTTON)

    @allure.step("Авторизоваться")
    def login(self, email, password):
        self.go_to_login_page()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        self.wait_for_url_not_contains("/login")

    @allure.step("Нажать ссылку 'Восстановить пароль'")
    def click_forgot_password_link(self):
        self.open_url(LOGIN_URL)
        self.click_element(self.locators.FORGOT_PASSWORD_LINK)