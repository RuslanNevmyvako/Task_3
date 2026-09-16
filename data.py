"""Конфигурационные данные для тестов"""

# URL
BASE_URL = "https://stellarburgers.education-services.ru"
LOGIN_URL = f"{BASE_URL}/login"
API_URL = f"{BASE_URL}/api"

# Таймауты
DEFAULT_TIMEOUT = 10
IMPLICIT_WAIT = 10

# Размеры окна
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

# Тестовые данные
TEST_EMAIL = "test@test.com"
TEST_PASSWORD = "Test123!"
TEST_NAME = "Test User"

# Сообщения об ошибках
ERROR_MESSAGES = {
    "invalid_credentials": "Некорректный email или пароль",
    "user_exists": "Пользователь уже существует",
    "required_fields": "Все поля обязательны для заполнения"
}