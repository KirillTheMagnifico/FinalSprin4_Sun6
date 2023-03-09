from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import pytest
# Создаем класс главной страницы и описываем локаторы
class HomePage:
    first_question = (By.ID, 'accordion__heading-0')
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

# Описываем методы проверки
    def check_question_one(self):
        return self.driver.find_element(*self.first_question)

    def check_question_two(self):
        return self.driver.find_element(*self.two_question)

    def check_question_three(self):
        return self.driver.find_element(*self.three_question)

    def check_question_fourth(self):
        return self.driver.find_element(*self.fourth_question)

    def check_question_five(self):
        return self.driver.find_element(*self.five_question)

    def check_question_six(self):
        return self.driver.find_element(*self.six_question)

    def check_question_seven(self):
        return self.driver.find_element(*self.seven_question)

    def check_question_eight(self):
        return self.driver.find_element(*self.eight_question)
