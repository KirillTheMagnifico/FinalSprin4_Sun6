from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import pytest

@pytest.fixture(scope="function")
def firefox_driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--width=800")
    firefox_options.add_argument("--height=800")
    driver = webdriver.Firefox(options=firefox_options)
    yield driver
    driver.quit()

