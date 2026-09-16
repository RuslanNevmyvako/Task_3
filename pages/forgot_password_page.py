import allure
from pages.base_page import BasePage
from locators.locators import ForgotPasswordPageLocators


class ForgotPasswordPage(BasePage):
    """Страница восстановления пароля"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ForgotPasswordPageLocators()
    
    @allure.step("Ввести email для восстановления")
    def enter_email(self, email):
        self.input_text(self.locators.EMAIL_INPUT, email)
    
    @allure.step("Нажать кнопку 'Восстановить'")
    def click_restore_button(self):
        self.click_element(self.locators.RESTORE_BUTTON)
    
    @allure.step("Нажать ссылку 'Войти'")
    def click_login_link(self):
        self.click_element(self.locators.LOGIN_LINK)
    
    @allure.step("Проверить, что форма восстановления отображается")
    def is_restore_form_displayed(self):
        return self.is_element_displayed(self.locators.EMAIL_INPUT)