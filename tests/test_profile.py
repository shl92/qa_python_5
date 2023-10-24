from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPage, ProfilePage, LoginPage


class TestProfile:
    def test_enter_profile(self, driver, login):
        driver.find_element(*MainPage.profile).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_contains('profile'))
        assert 'profile' in driver.current_url, (f"Ссылка не соответствует профилю, фактическая ссылка: "
                                                 f"{driver.current_url}")

    def test_logout_from_profile(self, driver, login):
        driver.find_element(*MainPage.profile).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_contains('profile'))
        driver.find_element(*ProfilePage.logout_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginPage.login_button))
        login_button = driver.find_element(*LoginPage.login_button).text
        assert login_button == "Войти", "Кнопка 'Войти' не найдена"

    def test_go_to_constructor_use_button(self, driver, login):
        driver.find_element(*MainPage.constructor_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPage.make_order))
        order_button = driver.find_element(*MainPage.make_order).text
        assert order_button == "Оформить заказ", "Кнопка 'Оформить заказ' не найдена"

    def test_go_to_constructor_use_logo(self, driver, login):
        driver.find_element(*MainPage.logo).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPage.make_order))
        order_button = driver.find_element(*MainPage.make_order).text
        assert order_button == "Оформить заказ", "Кнопка 'Оформить заказ' не найдена"
