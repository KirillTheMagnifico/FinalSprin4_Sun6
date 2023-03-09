from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import pytest
# Создаем класс главной страницы и описываем локаторы
class HomePage:
    first_question = (By.CLASS_NAME, 'accordion__button')
    two_question = (By.ID, 'accordion__heading-1')
    three_question = (By.ID, 'accordion__heading-2')
    fourth_question = (By.ID, 'accordion__heading-3')
    five_question = (By.ID, 'accordion__heading-4')
    six_question = (By.ID, 'accordion__heading-5')
    seven_question = (By.ID, 'accordion__heading-6')
    eight_question = (By.ID, 'accordion__heading-7')
    first_answer = (By.ID, 'accordion__panel-0')
    two_answer = (By.ID, 'accordion__panel-1')
    three_answer = (By.ID, 'accordion__panel-2')
    fourth_answer = (By.ID, 'accordion__panel-3')
    five_answer = (By.ID, 'accordion__panel-4')
    six_answer = (By.ID, 'accordion__panel-5')
    seven_answer = (By.ID, 'accordion__panel-6')
    eight_answer = (By.ID, 'accordion__panel-7')
    cookies = (By.XPATH, '// *[ @ id = "rcc-confirm-button"]')
    Order_high = (By.CLASS_NAME, 'Button_Button__ra12g')
    Order_Middle = (By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM')

# Вызываем фикстуру для браузера описанную в Conftest
    def __init__(self, firefox_driver):
        self.driver = firefox_driver
        self.page = 'https://qa-scooter.praktikum-services.ru/'



