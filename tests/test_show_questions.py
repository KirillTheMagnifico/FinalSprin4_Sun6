from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import allure
import pytest

# импортируем из файла Homepage класс и методы
from pages.HomePage import HomePage


# Подключаем Allure и создаем класс автотестов

class TestShowQuestion:
    @allure.feature('Домашняя страница')
    @allure.story('Вопросы')
    @allure.title('Проверить что все вопросы кликабельны')
    def test_show_home_page(self, firefox_driver):
        window = HomePage(firefox_driver)
        with allure.step(f'Открываем страницу {window.page}'):
            firefox_driver.get(window.page)
            firefox_driver.find_element(*window.cookies).click()
            WebDriverWait(firefox_driver, 20).until(ec.presence_of_element_located((By.TAG_NAME, "body")))
    def test_show_first_question(self, firefox_driver):
        window = HomePage(firefox_driver)
        with allure.step('кликаем на 1-й вопрос'):
             firefox_driver.get(window.page)
             firefox_driver.find_element(*window.cookies).click()
             WebDriverWait(firefox_driver, 20).until(ec.presence_of_element_located((By.TAG_NAME, "body")))
             element = firefox_driver.find_element(By.XPATH, '//div[@id="accordion__heading-0" and contains(text(), "Сколько это стоит? И как оплатить?")]')
             firefox_driver.execute_script("arguments[0].scrollIntoView();", element)
             actual_text = element.text
             expected_text = 'Сколько это стоит? И как оплатить?'
             assert actual_text == expected_text


    def test_show_two_question(self, firefox_driver):
        window = HomePage(firefox_driver)
        with allure.step('кликаем на 2-й вопрос'):
             firefox_driver.get(window.page)
             firefox_driver.find_element(*window.cookies).click()
             WebDriverWait(firefox_driver, 20).until(ec.presence_of_element_located((By.TAG_NAME, "body")))
             element = firefox_driver.find_element(By.XPATH,'//div[@id="accordion__heading-1" and contains(text(), "Хочу сразу несколько самокатов! Так можно?")]')
             firefox_driver.execute_script("arguments[0].scrollIntoView();", element)
             WebDriverWait(firefox_driver, 5).until(ec.presence_of_element_located(window.two_question)).click()
             active = element.is_enabled() and element.is_displayed() and element.get_attribute('aria-expanded') == 'true'
             assert active is True, "Элемент не активен"


    def test_show_three_question(self, firefox_driver):
        window = HomePage(firefox_driver)
        with allure.step('кликаем на 3-й вопрос'):
             firefox_driver.get(window.page)
             firefox_driver.find_element(*window.cookies).click()
             WebDriverWait(firefox_driver, 20).until(ec.presence_of_element_located((By.TAG_NAME, "body")))
             element = firefox_driver.find_element(By.XPATH, '//div[@id="accordion__heading-2" and contains(text(), "Как рассчитывается время аренды?")]')
             firefox_driver.execute_script("arguments[0].scrollIntoView();", element)
             WebDriverWait(firefox_driver, 5).until(ec.presence_of_element_located(window.three_question)).click()
             active = element.is_enabled() and element.is_displayed() and element.get_attribute('aria-expanded') == 'true'
             assert active is True, 'Элемент не активен'
    def test_show_fourth_question(self, firefox_driver):
        window = HomePage(firefox_driver)
        with allure.step('кликаем на 4-й вопрос'):
             firefox_driver.get(window.page)
             firefox_driver.find_element(*window.cookies).click()
             WebDriverWait(firefox_driver, 20).until(ec.presence_of_element_located((By.TAG_NAME, "body")))
             element = firefox_driver.find_element(By.XPATH, '//div[@id="accordion__heading-3" and contains(text(), "Можно ли заказать самокат прямо на сегодня?")]')
             firefox_driver.execute_script("arguments[0].scrollIntoView();", element)
             WebDriverWait(firefox_driver, 5).until(ec.presence_of_element_located(window.fourth_question)).click()
             active = element.is_enabled() and element.is_displayed() and element.get_attribute('aria-expanded') == 'true'
             assert active is True, "Элемент не активен"
    def test_show_five_question(self, firefox_driver):
        window = HomePage(firefox_driver)
        with allure.step('кликаем на 5-й вопрос'):
            firefox_driver.get(window.page)
            firefox_driver.find_element(*window.cookies).click()
            WebDriverWait(firefox_driver, 20).until(ec.presence_of_element_located((By.TAG_NAME, "body")))
            element = firefox_driver.find_element(By.XPATH, '//div[@id="accordion__heading-4" and contains(text(), "Можно ли продлить заказ или вернуть самокат раньше?")]')
            firefox_driver.execute_script("arguments[0].scrollIntoView();", element)
            WebDriverWait(firefox_driver, 5).until(ec.presence_of_element_located(window.five_question)).click()
            active = element.is_enabled() and element.is_displayed() and element.get_attribute('aria-expanded') == 'true'
            assert active is True, "Элемент не активен"
    def test_show_six_question(self, firefox_driver):
        window = HomePage(firefox_driver)
        with allure.step('кликаем на 6-й вопрос'):
            firefox_driver.get(window.page)
            firefox_driver.find_element(*window.cookies).click()
            WebDriverWait(firefox_driver, 20).until(ec.presence_of_element_located((By.TAG_NAME, "body")))
            element = firefox_driver.find_element(By.XPATH, '//div[@id="accordion__heading-5" and contains(text(), "Вы привозите зарядку вместе с самокатом?")]')
            firefox_driver.execute_script("arguments[0].scrollIntoView();", element)
            WebDriverWait(firefox_driver, 5).until(ec.presence_of_element_located(window.six_question)).click()
            active = element.is_enabled() and element.is_displayed() and element.get_attribute('aria-expanded') == 'true'
            assert active is True, "Элемент не активен"
    def test_show_seven_question(self, firefox_driver):
        window = HomePage(firefox_driver)
        with allure.step('кликаем на 7-й вопрос'):
            firefox_driver.get(window.page)
            firefox_driver.find_element(*window.cookies).click()
            WebDriverWait(firefox_driver, 20).until(ec.presence_of_element_located((By.TAG_NAME, "body")))
            element = firefox_driver.find_element(By.XPATH, '//div[@id="accordion__heading-6" and contains(text(), "Можно ли отменить заказ?")]')
            firefox_driver.execute_script("arguments[0].scrollIntoView();", element)
            WebDriverWait(firefox_driver, 5).until(ec.presence_of_element_located(window.seven_question)).click()
            active = element.is_enabled() and element.is_displayed() and element.get_attribute('aria-expanded') == 'true'
            assert active is True, "Элемент не активен"
    def test_show_eight_question(self, firefox_driver):
        window = HomePage(firefox_driver)
        with allure.step('кликаем на 8-й вопрос'):
            firefox_driver.get(window.page)
            firefox_driver.find_element(*window.cookies).click()
            WebDriverWait(firefox_driver, 20).until(ec.presence_of_element_located((By.TAG_NAME, "body")))
            element = firefox_driver.find_element(By.XPATH, '//div[@id="accordion__heading-7" and contains(text(), "Я жизу за МКАДом, привезёте?")]')
            firefox_driver.execute_script("arguments[0].scrollIntoView();", element)
            WebDriverWait(firefox_driver, 5).until(ec.presence_of_element_located(window.eight_question)).click()
            active = element.is_enabled() and element.is_displayed() and element.get_attribute('aria-expanded') == 'true'
            assert active is True, "Элемент не активен"
