import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import Urls, Data
from support_functions import Generators
from locators import RegistrationPage


class TestRegistration:
    def test_registration_new_user_create(self, driver):
        driver.get(Urls.REGISTER_PAGE)
        driver.find_element(*RegistrationPage.name_input).send_keys(Data.NAME)
        driver.find_element(*RegistrationPage.email_input).send_keys(Generators.generate_email())
        driver.find_element(*RegistrationPage.password_input).send_keys(Generators.generate_password())
        driver.find_element(*RegistrationPage.registration_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_contains(Urls.LOGIN_PAGE))
        assert driver.current_url == Urls.LOGIN_PAGE, (f"Ожидаемый URL: {Urls.LOGIN_PAGE}, "
                                                       f"фактический URL: {driver.current_url}")

    def test_registration_incorrect_password_less_then_6_chars_error(self, driver):
        driver.get(Urls.REGISTER_PAGE)
        driver.find_element(*RegistrationPage.name_input).send_keys(Data.NAME)
        driver.find_element(*RegistrationPage.email_input).send_keys(Generators.generate_email())
        driver.find_element(*RegistrationPage.password_input).send_keys(Generators.generate_password(5))
        driver.find_element(*RegistrationPage.registration_button).click()
        error = driver.find_element(*RegistrationPage.error_password_text).text
        assert error == "Некорректный пароль", f"Ожидаемый текст ошибки: Некорректный пароль, Фактически: {error}"

    @pytest.mark.parametrize('name, email, password',
                             [(Data.EMPTY_FIELD, Generators.generate_email(), Generators.generate_password(7)),
                              (Data.NAME, Data.EMPTY_FIELD, Generators.generate_password(6)),
                              (Data.NAME, Generators.generate_email(), Generators.generate_password(0))],
                             ids=['EmptyName', 'EmptyEmail', 'EmptyPassword'])
    def test_registration_no_name_no_email_no_password(self, driver, name, email, password):
        driver.get(Urls.REGISTER_PAGE)
        driver.find_element(*RegistrationPage.name_input).send_keys(name)
        driver.find_element(*RegistrationPage.email_input).send_keys(email)
        driver.find_element(*RegistrationPage.password_input).send_keys(password)
        driver.find_element(*RegistrationPage.registration_button).click()
        assert driver.current_url == Urls.REGISTER_PAGE, (f"Ожидаемый URL: {Urls.REGISTER_PAGE}, "
                                                          f"фактический URL: {driver.current_url}")

    def test_registration_the_same_user_error(self, driver):
        driver.get(Urls.REGISTER_PAGE)
        driver.find_element(*RegistrationPage.name_input).send_keys(Data.NAME)
        driver.find_element(*RegistrationPage.email_input).send_keys(Data.EMAIL)
        driver.find_element(*RegistrationPage.password_input).send_keys(Data.PASSWORD)
        driver.find_element(*RegistrationPage.registration_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(RegistrationPage.error_exist_user))
        error = driver.find_element(*RegistrationPage.error_exist_user).text
        assert error == "Такой пользователь уже существует", (f"Ожидаемая ошибка: {error}, факт: регистрация "
                                                              f"уже существующего пользователя")
