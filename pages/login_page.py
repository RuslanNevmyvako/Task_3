import allure
from pages.base_page import BasePage
from locators.locators import LoginPageLocators
from data import BASE_URL


class LoginPage(BasePage):
    """Страница входа"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators()

    @allure.step("Перейти на страницу входа")
    def go_to_login_page(self):
        from pages.main_page import MainPage
        MainPage(self.driver).click_profile()
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

    @allure.step("Нажать кнопку 'Войти'")
    def click_login_button(self):
        self.click_element(self.locators.LOGIN_BUTTON)

    @allure.step("Авторизоваться")
    def login(self, email, password):
        self.go_to_login_page()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        # ← ждём, что ушли со страницы логина
        self.wait.until(lambda d: "/login" not in d.current_url)

    @allure.step("Нажать ссылку 'Восстановить пароль'")
    def click_forgot_password_link(self):
        self.driver.get(f"{BASE_URL}/login")
        self.click_element(self.locators.FORGOT_PASSWORD_LINK)