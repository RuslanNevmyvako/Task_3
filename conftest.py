# conftest.py
import time
import pytest
from driver_factory import DriverFactory
import requests
from faker import Faker
from data import API_URL, BASE_URL

fake = Faker()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--headless", action="store_true")


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    print(f"\n🚀 Запуск теста в браузере: {browser}")
    driver = DriverFactory.get_driver(browser, headless)
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def create_user_via_api():
    timestamp = int(time.time() * 1000)
    user_data = {
        "email": f"test_{timestamp}@test.com",
        "password": "TestPass123!",
        "name": f"User_{timestamp}"
    }

    response = requests.post(f"{API_URL}/auth/register", json=user_data)

    if response.status_code != 200:
        pytest.skip(f"Не удалось создать пользователя: {response.text}")

    response_data = response.json()
    access_token = response_data.get("accessToken", "")
    if access_token and access_token.startswith("Bearer "):
        access_token = access_token.replace("Bearer ", "")

    yield {
        "data": user_data,
        "access_token": access_token,
        "full_token": response_data.get("accessToken")
    }


@pytest.fixture(scope="function")
def create_order_via_api(create_user_via_api):
    response = requests.get(f"{API_URL}/ingredients")
    if response.status_code != 200:
        pytest.skip("Не удалось получить ингредиенты")

    ingredients = response.json()["data"]
    ingredient_ids = [ing["_id"] for ing in ingredients[:2]]

    token = create_user_via_api["access_token"]
    response = requests.post(
        f"{API_URL}/orders",
        json={"ingredients": ingredient_ids},
        headers={"Authorization": f"Bearer {token}"}
    )

    if response.status_code != 200:
        pytest.skip(f"Не удалось создать заказ: {response.text}")

    return response.json()