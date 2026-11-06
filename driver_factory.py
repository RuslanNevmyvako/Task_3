# driver_factory.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:
    """Фабрика для создания драйверов браузеров"""
    
    @staticmethod
    def get_driver(browser_name="chrome", headless=False):
        """
        Создает и возвращает драйвер для указанного браузера.
        
        Args:
            browser_name: Название браузера ("chrome" или "firefox")
            headless: Запускать ли браузер в headless-режиме
        
        Returns:
            WebDriver: Экземпляр драйвера
        """
        browser_name = browser_name.lower()
        
        if browser_name == "chrome":
            return DriverFactory._create_chrome_driver(headless)
        elif browser_name == "firefox":
            return DriverFactory._create_firefox_driver(headless)
        else:
            raise ValueError(f"Неподдерживаемый браузер: {browser_name}. Поддерживаемые: chrome, firefox")
    
    @staticmethod
    def _create_chrome_driver(headless=False):
        """Создание драйвера для Chrome"""
        options = ChromeOptions()
        
        if headless:
            options.add_argument("--headless=new")
        
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions")
        
        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)
    
    @staticmethod
    def _create_firefox_driver(headless=False):
        """Создание драйвера для Firefox"""
        options = FirefoxOptions()
        
        if headless:
            options.add_argument("--headless")
        
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        
        service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service, options=options)