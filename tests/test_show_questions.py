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
        page = HomePage(firefox_driver)
        with allure.step(f'Открываем страницу {page.page}'):
            firefox_driver.get(page.page)
            firefox_driver.find_element(*page.cookies).click()
            WebDriverWait(firefox_driver, 10).until(ec.presence_of_element_located((By.TAG_NAME, "body")))
            element = firefox_driver.find_element(By.XPATH, '//div[@id="accordion__heading-0" and contains(text(), "Сколько это стоит? И как оплатить?")]')
            firefox_driver.execute_script("arguments[0].scrollIntoView();", element)
    def test_show_first_question(self, firefox_driver):
        with allure.step('кликаем на 1-й вопрос'):
             WebDriverWait(firefox_driver, 10).until(ec.presence_of_element_located(page.first_question)).click()
             WebDriverWait(firefox_driver, 10).until(ec.presence_of_element_located(page.first_answer))
             text = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
             assert text in firefox_driver.find_element(page.first_answer).text


    def test_show_two_question(self, firefox_driver):
        with allure.step('кликаем на 2-й вопрос'):
             WebDriverWait(firefox_driver, 10).until(ec.presence_of_element_located(page.two_question)).click()
             WebDriverWait(firefox_driver, 10).until(ec.presence_of_element_located(page.two_answer))
             text = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
             assert text in firefox_driver.find_element(page.two_answer).text


    def test_show_three_question(self, firefox_driver):
        with allure.step('кликаем на 3-й вопрос'):
             WebDriverWait(firefox_driver, 10).until(ec.presence_of_element_located(page.three_question)).click()
             WebDriverWait(firefox_driver, 10).until(ec.presence_of_element_located(page.three_answer))
             text = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
             assert text in firefox_driver.find_element(page.three_answer).text
    def test_show_fourth_question(self, firefox_driver):
        with allure.step('кликаем на 4-й вопрос'):
             WebDriverWait(firefox_driver, 10).until(ec.presence_of_element_located(page.fourth_question)).click()
             WebDriverWait(firefox_driver, 10).until(ec.presence_of_element_located(page.fourth_answer))
             text = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
             assert text in firefox_driver.find_element(page.fourth_answer).text
    def test_show_five_question(self, firefox_driver):
        with allure.step('кликаем на 5-й вопрос'):
            WebDriverWait(firefox_driver, 10).until(ec.presence_of_element_located(page.five_question)).click()
            WebDriverWait(firefox_driver, 10).until(ec.presence_of_element_located(page.five_answer))
            text = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
            assert text in firefox_driver.find_element(page.five_answer).text
    def test_show_six_question(self, firefox_driver):
        with allure.step('кликаем на 6-й вопрос'):
            WebDriverWait(firefox_driver, 10).until(ec.presence_of_element_located(page.six_question)).click()
            WebDriverWait(firefox_driver, 10).until(ec.presence_of_element_located(page.six_answer))
            text = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
            assert text in firefox_driver.find_element(page.six_answer).text
    def test_show_seven_question(self, firefox_driver):
        with allure.step('кликаем на 7-й вопрос'):
            WebDriverWait(firefox_driver, 10).until(ec.presence_of_element_located(page.seven_question)).click()
            WebDriverWait(firefox_driver, 10).until(ec.presence_of_element_located(page.seven_answer))
            text = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
            assert text in firefox_driver.find_element(page.seven_answer).text
    def test_show_eight_question(self, firefox_driver):
        with allure.step('кликаем на 8-й вопрос'):
            WebDriverWait(firefox_driver, 10).until(ec.presence_of_element_located(page.eight_question)).click()
            WebDriverWait(firefox_driver, 10).until(ec.presence_of_element_located(page.eight_answer))
            text = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
            assert text in firefox_driver.find_element(page.eight_answer).text
