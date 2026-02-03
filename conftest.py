import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from utils.config_reader import load_config
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def config():
    return load_config()

@pytest.fixture(scope="session")
def driver(config):
    browser = config["browser"].lower()

    if browser == "chrome":
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
    else:
        raise ValueError(f"Browser '{browser}' is not supported")
    driver.maximize_window()
    driver.get(config["base_url"])
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver, config):
    """
    Logs into the application and returns driver
    """
    driver.get(config["base_url"])

    login_page = LoginPage(driver)
    login_page.login(
        config["credentials"]["username"],
        config["credentials"]["password"]
    )

    time.sleep(10)
    alert = driver.switch_to.alert()
    alert.accept()
    return driver