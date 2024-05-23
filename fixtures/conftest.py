import requests
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from Diplom_3.fixtures import generate_user_credentials, register_user as api_register_user
from Diplom_3.pages.feed_page import FeedPage
from Diplom_3.pages.main_page import MainPage
from Diplom_3.pages.login_page import LoginPage
from Diplom_3.pages.reset_password_page import ResetPasswordPage
from Diplom_3.fixtures import URL_AUTH_REGISTER, URL_HOME, URL_LOGIN, URL_RESET_PASSWORD, URL_FORGOT_PASSWORD, URL_ORDERS_FEED


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        firefox_driver = GeckoDriverManager().install()
        service = FirefoxService(firefox_driver)
        driver = webdriver.Firefox(service=service)
    else:
        chrome_driver = ChromeDriverManager().install()
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

    yield driver
    driver.quit()


# Фикстура для генерации учетных данных пользователя
@pytest.fixture()
def generate_user():
    """
    Генерирует учетные данные пользователя.
    Возвращает словарь с учетными данными.
    """
    return generate_user_credentials()

# Фикстура для регистрации пользователя через API
@pytest.fixture()
def register_user(generate_user):
    """
    Регистрирует пользователя через API.
    Возвращает словарь с учетными данными.
    """
    credentials = generate_user
    api_register_user(credentials)
    return {
        'credentials': credentials
    }


# Фикстура для удаления созданного пользователя
@pytest.fixture()
def delete_registered_user(register_user):
    """
    Удаляет пользователя, созданного в фикстуре register_user.
    """
    credentials = register_user['credentials']
    requests.delete(URL_AUTH_REGISTER, json=credentials)


@pytest.fixture()
def main_page(driver):
    """
    Открывает главную страницу и возвращает экземпляр MainPage.
    """
    driver.get(URL_HOME)
    return MainPage(driver)


@pytest.fixture()
def login_page(driver):
    """
    Открывает страницу входа и возвращает экземпляр LoginPage.
    """
    driver.get(URL_LOGIN)
    return LoginPage(driver)


@pytest.fixture()
def reset_password_page(driver):
    """
    Открывает страницу сброса пароля и возвращает экземпляр ResetPasswordPage.
    """
    driver.get(URL_RESET_PASSWORD)
    return ResetPasswordPage(driver)


@pytest.fixture()
def forgot_password_page(driver):
    """
    Открывает страницу восстановления пароля и возвращает экземпляр ResetPasswordPage.
    """
    driver.get(URL_FORGOT_PASSWORD)
    return ResetPasswordPage(driver)


@pytest.fixture()
def feed_page(driver):
    """
    Открывает страницу ленты заказов и возвращает экземпляр FeedPage.
    """
    driver.get(URL_ORDERS_FEED)
    return FeedPage(driver)


# Фикстура для авторизации пользователя
@pytest.fixture()
def authorize_user(driver, register_user, login_page):
    """
    Авторизует пользователя с использованием предоставленных учетных данных.
    Возвращает словарь с учетными данными и экземпляром MainPage.
    """
    credentials = register_user['credentials']
    login_page.get_email_input().send_keys(credentials['email'])
    login_page.get_password_input().send_keys(credentials['password'])
    login_page.get_enter_button().click()
    login_page.wait_for_url(5, URL_HOME)
    return {
        'credentials': credentials,
        'main_page': MainPage(driver)
    }
