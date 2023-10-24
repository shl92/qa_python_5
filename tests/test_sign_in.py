from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constants import Urls, Data
from locators import MainPage, LoginPage


class TestSignIn:

    def test_sign_in_from_main_page(self, driver):
        driver.get(Urls.MAIN_PAGE)
        driver.find_element(*MainPage.login_button).click()
        driver.find_element(*LoginPage.email_input).send_keys(Data.EMAIL)
        driver.find_element(*LoginPage.password_input).send_keys(Data.PASSWORD)
        driver.find_element(*LoginPage.login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPage.make_order))
        order_button = driver.find_element(*MainPage.make_order).text
        assert order_button == "Оформить заказ", "Кнопка 'Оформить заказ' не найдена"

    def test_sign_in_from_profile(self, driver):
        driver.get(Urls.MAIN_PAGE)
        driver.find_element(*MainPage.profile).click()
        driver.find_element(*LoginPage.email_input).send_keys(Data.EMAIL)
        driver.find_element(*LoginPage.password_input).send_keys(Data.PASSWORD)
        driver.find_element(*LoginPage.login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPage.make_order))
        order_button = driver.find_element(*MainPage.make_order).text
        assert order_button == "Оформить заказ", "Кнопка 'Оформить заказ' не найдена"

    def test_sign_in_from_registration_page(self, driver):
        driver.get(Urls.REGISTER_PAGE)
        driver.find_element(*MainPage.login_href).click()
        driver.find_element(*LoginPage.email_input).send_keys(Data.EMAIL)
        driver.find_element(*LoginPage.password_input).send_keys(Data.PASSWORD)
        driver.find_element(*LoginPage.login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPage.make_order))
        order_button = driver.find_element(*MainPage.make_order).text
        assert order_button == "Оформить заказ", "Кнопка 'Оформить заказ' не найдена"

    def test_sign_in_from_recover_password_page(self, driver):
        driver.get(Urls.RECOVERY_PAGE)
        driver.find_element(*MainPage.login_href).click()
        driver.find_element(*LoginPage.email_input).send_keys(Data.EMAIL)
        driver.find_element(*LoginPage.password_input).send_keys(Data.PASSWORD)
        driver.find_element(*LoginPage.login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPage.make_order))
        order_button = driver.find_element(*MainPage.make_order).text
        assert order_button == "Оформить заказ", "Кнопка 'Оформить заказ' не найдена"
