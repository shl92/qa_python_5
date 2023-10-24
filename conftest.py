import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import Urls, Data
from locators import LoginPage, MainPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.get(Urls.LOGIN_PAGE)
    driver.find_element(*LoginPage.email_input).send_keys(Data.EMAIL)
    driver.find_element(*LoginPage.password_input).send_keys(Data.PASSWORD)
    driver.find_element(*LoginPage.login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPage.make_order))
    return driver
