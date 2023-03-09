from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import pytest

class OrderPage:

    name = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/input')
    surname = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/input')
    adress = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[3]/input')
    station = (By.CLASS_NAME, 'select-search__input')
    station_value = (By.CLASS_NAME, 'select-search__input')
    phone = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[5]/input')
    next = (By.XPATH, '/html/body/div/div/div[2]/div[3]/button')
    calendar = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/div/div/input')
    day = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[3]')
    arenda = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div[1]')
    srok = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div[2]')
    checkbox = (By.XPATH, '//*[@id="black"]')
    order_button = (By.XPATH, '/html/body/div/div/div[2]/div[3]/button[2]')
    button_yes = (By.XPATH, '/html/body/div/div/div[2]/div[5]/div[2]/button[2]')
    ok = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
    order_status = (By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM')
    yandex_logo = (By.CSS_SELECTOR, '.Header_LogoYandex__3TSOI > img:nth-child(1)')
    samokat_logo = (By.CSS_SELECTOR, '.Header_LogoScooter__3lsAR > img:nth-child(1)')
    home_page = ('https://qa-scooter.praktikum-services.ru/')

    def __init__(self, firefox_driver):
        self.driver = firefox_driver
        self.page = 'https://qa-scooter.praktikum-services.ru/order'

    def set_name(self):
        self.driver.find_element(*self.name).send_keys('Кирилл')
    def set_surname(self):
        self.driver.find_element(*self.surname).send_keys('Тищенко')
    def set_adress(self):
        self.driver.find_element(*self.adress).send_keys('г. Москва, Зорге 36')
    def click_station(self):
        self.driver.find_element(*self.station).click()
    def set_station(self):
        self.driver.find_element(*self.station).send_keys('Выхино')
    def choose_station(self):
        self.driver.find_element(*self.vihino).click()
    def set_phone(self):
        self.driver.find_element(*self.phone).send_keys('79850600206')
    def next_step(self):
        self.driver.find_element(*self.next).click()
    def set_registration(self, name, surname, adress, station, vihino, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_adress(adress)
        self.set_station(station)
        self.choose_station(vihino)
        self.set_phone(phone)
        self.driver.find_element(*self.next).click()
    def calendar_visible(self):
        self.driver.find_element(*self.calendar).click()
    def choose_a_date(self):
        self.driver.find_element(*self.day).click()
    def arenda_samokat(self):
        self.driver.find_element(*self.arenda).click()
    def set_a_srok(self):
        self.driver.find_element(*self.srok).click()
    def set_checkbox(self):
        self.driver.find_element(*self.checkbox).click()
    def click_order(self):
        self.driver.find_element(*self.order_button).click()
    def click_yes(self):
        self.driver.find_element(*self.button_yes).click()
    def positive_order(self, calendar, day, arenda, srok, checkbox):
        self.calendar_visible(calendar)
        self.Choose_a_date(day)
        self.arenda_samokat(arenda)
        self.set_a_srok(srok)
        self.set_checkbox(checkbox)
        self.driver.find_element(*self.order_button).click()
        self.driver.find_element(*self.button_yes).click()
