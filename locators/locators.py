from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Локаторы страницы входа"""
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")


class MainPageLocators:
    """Локаторы главной страницы"""
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[@href='/']")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[@href='/feed']")
    PROFILE_BUTTON = (By.XPATH, "//a[@href='/account']")

    BUN_INGREDIENT = (By.XPATH, "//h2[text()='Булки']/following-sibling::ul[1]//a[contains(@class, 'BurgerIngredient_ingredient')]")
    SAUCE_INGREDIENT = (By.XPATH, "//h2[text()='Соусы']/following-sibling::ul[1]//a[contains(@class, 'BurgerIngredient_ingredient')]")
    FILLING_INGREDIENT = (By.XPATH, "//h2[text()='Начинки']/following-sibling::ul[1]//a[contains(@class, 'BurgerIngredient_ingredient')]")

    INGREDIENT_COUNTER = (By.XPATH, ".//p[contains(@class, 'counter_counter__num')]")

    # Drop-зоны конструктора
    BUN_TOP_DROP_ZONE = (By.XPATH, "//*[contains(text(), 'Перетяните булочку сюда (верх)')]/..")
    BUN_BOTTOM_DROP_ZONE = (By.XPATH, "//*[contains(text(), 'Перетяните булочку сюда (низ)')]/..")
    
    # Зона для соусов и начинок — контейнер бургера целиком
    BASKET_LIST = (By.XPATH, "//span[contains(@class, 'BurgerConstructor_basket__listContainer')]")

    # Модалки
    INGREDIENT_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    INGREDIENT_MODAL_CLOSE = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]")
    ORDER_NUMBER_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//p[text()='идентификатор заказа']")
    ORDER_NUMBER = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//h2[contains(@class, 'text_type_digits-large')]")

    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    ORDER_NUMBER_MODAL_CLOSE = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]")

class ProfilePageLocators:
    """Локаторы страницы профиля"""
    PROFILE_LINK = (By.XPATH, "//a[@href='/account/profile']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[@href='/account/order-history']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    ORDER_IN_HISTORY = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]")
    ORDER_NUMBER_IN_HISTORY = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")

class OrderFeedPageLocators:
    """Локаторы страницы ленты заказов"""
    ORDER_ITEM = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]")
    ORDER_LINK = (By.XPATH, "//a[contains(@class, 'OrderHistory_link')]")

    ORDER_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    ORDER_MODAL_CLOSE = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]")
    ORDER_NUMBER_IN_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//h2[contains(@class, 'text_type_digits-large')]")

    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]//li[contains(@class, 'text_type_digits-default')]")


class ForgotPasswordPageLocators:
    """Локаторы страницы восстановления пароля"""
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")

class ResetPasswordPageLocators:
    """Локаторы страницы сброса пароля"""
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Введите новый пароль']")
    SHOW_PASSWORD_BUTTON = (By.CSS_SELECTOR, "div.input__icon-action")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")