import allure
from pages.base_page import BasePage
from locators.locators import ResetPasswordPageLocators


class ResetPasswordPage(BasePage):
    """Страница сброса пароля"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ResetPasswordPageLocators()
    
    @allure.step("Ввести новый пароль")
    def enter_new_password(self, password):
        element = self.wait_for_element_visible(self.locators.PASSWORD_INPUT)
        element.clear()
        element.send_keys(password)
    
    @allure.step("Нажать кнопку показать/скрыть пароль")
    def click_show_password_button(self):
        self.click_element(self.locators.SHOW_PASSWORD_BUTTON)
    
    @allure.step("Нажать кнопку 'Сохранить'")
    def click_save_button(self):
        self.click_element(self.locators.SAVE_BUTTON)
    
    @allure.step("Проверить, что поле пароля активно (в фокусе)")
    def is_password_field_active(self):
        """Проверяет, что поле пароля получило фокус (подсвечено)"""
        element = self.find_element(self.locators.PASSWORD_INPUT)
        # Проверяем через JavaScript, что именно это поле в фокусе
        return self.driver.execute_script(
            "return document.activeElement === arguments[0];", element
        )
    
    @allure.step("Проверить, что страница сброса пароля отображается")
    def is_reset_page_displayed(self):
        return self.is_element_displayed(self.locators.PASSWORD_INPUT)