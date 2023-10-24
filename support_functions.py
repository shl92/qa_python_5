import random
from string import ascii_letters


class Generators:
    digits = '0123456789'

    @staticmethod
    def generate_email():
        """Генерирует e-mail из букв и цифр длинной 7 символов + окончание @ya.ru, итого 13 символов"""
        name = random.sample(ascii_letters + Generators.digits, 7)
        return ''.join(name) + '@ya.ru'

    @staticmethod
    def generate_password(numbers=6):
        """Генерирует пароль длинною numbers символов, по умолчанию длинною в 6 символов"""
        return ''.join(random.sample(Generators.digits, numbers))
