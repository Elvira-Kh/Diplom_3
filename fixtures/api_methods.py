import allure
import random
import requests
import string

from Diplom_3.urls import URL_AUTH_REGISTER


@allure.step('Генерируем учётные данные пользователя')
def generate_user_credentials(exclude_email=False, exclude_password=False, exclude_name=False) -> dict:
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    credentials = {}

    if not exclude_email:
        credentials['email'] = generate_random_string(8) + '@ya.ru'

    if not exclude_password:
        credentials['password'] = generate_random_string(12)

    if not exclude_name:
        credentials['name'] = generate_random_string(8)

    return credentials


@allure.step('Регистрируем пользователя')
def register_user(credentials) -> requests.Response:
    return requests.post(URL_AUTH_REGISTER, json=credentials)

