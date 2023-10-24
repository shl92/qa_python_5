from selenium.webdriver.common.by import By


class RegistrationPage:
    name_input = (By.XPATH, "//fieldset[1]//input")  # Поле для ввода имени
    email_input = (By.XPATH, "//fieldset[2]//input")  # Поле для ввода e-mail
    password_input = (By.XPATH, "//input[@name='Пароль']")  # Поле для ввода пароля
    registration_button = (By.XPATH, "//form/button")  # Кнопка регистрации
    error_password_text = (By.XPATH, "//p[text()='Некорректный пароль']")  # Ошибка о некорректном пароле
    error_exist_user = (By.XPATH, "//p[text()='Такой пользователь уже существует']")  # Ошибка 'пользователь существует'


class LoginPage:
    email_input = (By.NAME, "name")  # Поле для ввода e-mail
    password_input = (By.NAME, "Пароль")  # Поле для ввода пароля
    login_button = (By.XPATH, "//button[text()='Войти']")  # Кнопка входа


class MainPage:
    login_button = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    profile = (By.XPATH, "//p[text()='Личный Кабинет']")  # Ссылка - Вход в личный кабинет
    login_href = (By.LINK_TEXT, 'Войти')  # Ссылка "Войти" на страницах сайта
    make_order = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка "Оформить заказ"
    constructor_button = (By.XPATH, "//p[text()='Конструктор']")  # Ссылка Конструктор в шапке сайта
    logo = (By.XPATH, "//div[contains(@class, 'header__logo')]")  # Логотип сайта (ссылка)
    bread_active = (By.XPATH, "//span[text()='Булки']/parent::*")  # Конструктор - кнопка "булки"
    sauces_active = (By.XPATH, "//span[text()='Соусы']/parent::*")  # Конструктор - кнопка "Соусы
    fillings_active = (By.XPATH, "//span[text()='Начинки']/parent::*")  # Конструктор - кнопка "Начинки"


class ProfilePage:
    logout_button = (By.XPATH, "//button[text()='Выход']")  # Кнопка выхода из профиля
