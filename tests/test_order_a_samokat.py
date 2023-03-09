from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import allure
import pytest
from selenium.webdriver.common.keys import Keys
from pages.OrderPage import OrderPage


class TestOrderASamokat:
    @allure.feature('Домашняя страница')
    def test_order_a_samokat(self, firefox_driver):
        page = OrderPage(firefox_driver)
        with allure.step(f'Открываем страницу {page.page}'):
            firefox_driver.get(page.page)
        with allure.step('Вводим необходимые данные для регистрации'):
            firefox_driver.find_element(*page.name).send_keys('Кирилл')
            firefox_driver.find_element(*page.surname).send_keys('Тищенко')
            firefox_driver.find_element(*page.adress).send_keys('г. Москва, Зорге 36')
        with allure.step('вводим станцию метро и телефон'):
            firefox_driver.find_element(*page.station).click()
            firefox_driver.find_element(*page.station).send_keys('Выхино')
            firefox_driver.find_element(*page.station).send_keys(Keys.ARROW_DOWN)
            firefox_driver.find_element(*page.station).send_keys(Keys.RETURN)
            firefox_driver.find_element(*page.phone).send_keys('79850600206')
            firefox_driver.find_element(*page.next).click()
        with allure.step('Заполняем чекбокс самоката и выбираем дату доставки'):
            firefox_driver.find_element(*page.calendar).send_keys('08.03.2023')
            firefox_driver.find_element(*page.day).click()
            firefox_driver.find_element(*page.arenda).click()
            firefox_driver.find_element(*page.srok).click()
            firefox_driver.find_element(*page.checkbox).click()
            firefox_driver.find_element(*page.order_button).click()
            firefox_driver.find_element(*page.button_yes).click()
            text = 'Заказ оформлен'
            assert text in firefox_driver.find_element(*page.ok).text


    def test_clickable_logo_samokat(self, firefox_driver):
        page = OrderPage(firefox_driver)
        firefox_driver.get(page.page)
        with allure.step('Проверим что при клике на лого Самоката мы останемся на главной'):
            firefox_driver.find_element(*page.samokat_logo).click()
            current_url = page.home_page
            expected_url = page.home_page
            assert current_url == expected_url

    def test_clickable_logo_yandex(self, firefox_driver):
        page = OrderPage(firefox_driver)
        firefox_driver.get(page.page)
        with allure.step('Проверим что при клике на лого Яндекса мы перейдем на другую страницу'):
            firefox_driver.find_element(*page.yandex_logo).click()
            current_url = 'https://dzen.ru/?yredirect=true'
            expected_url = 'https://dzen.ru/?yredirect=true'
            assert current_url == expected_url

