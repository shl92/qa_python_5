from locators import MainPage


class TestConstructor:
    def test_go_to_bread(self, driver, login):
        driver.find_element(*MainPage.fillings_active).click()
        active_button = driver.find_element(*MainPage.bread_active)
        active_button.click()
        assert 'current' in active_button.get_attribute('class'), f"Кнопка '{active_button.text}' не активна"

    def test_go_to_sauces(self, driver, login):
        active_button = driver.find_element(*MainPage.sauces_active)
        active_button.click()
        assert 'current' in active_button.get_attribute('class'), f"Кнопка '{active_button.text}' не активна"

    def test_go_to_fillings(self, driver, login):
        active_button = driver.find_element(*MainPage.fillings_active)
        active_button.click()
        assert 'current' in active_button.get_attribute('class'), f"Кнопка '{active_button.text}' не активна"
