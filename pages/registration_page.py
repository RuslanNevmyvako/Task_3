import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    """Страница регистрации"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RegistrationPageLocators()
    
    @allure.step("Ввести имя")
    def enter_name(self, name):
        self.input_text(self.locators.NAME_INPUT, name)
    
    @allure.step("Ввести email")
    def enter_email(self, email):
        self.input_text(self.locators.EMAIL_INPUT, email)
    
    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.input_text(self.locators.PASSWORD_INPUT, password)
    
    @allure.step("Нажать кнопку 'Зарегистрироваться'")
    def click_register_button(self):
        self.click_element(self.locators.REGISTER_BUTTON)
    
    @allure.step("Нажать ссылку 'Войти'")
    def click_login_link(self):
        self.click_element(self.locators.LOGIN_LINK)
    
    @allure.step("Зарегистрировать нового пользователя")
    def register_user(self, name, email, password):
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password)
        self.click_register_button()
    
    @allure.step("Получить сообщение об ошибке")
    def get_error_message(self):
        """Получение сообщения об ошибке регистрации"""
        try:
            # Используем локатор из locators, если он есть
            error_element = self.find_element(self.locators.ERROR_MESSAGE)
            return error_element.text
        except:
            return None