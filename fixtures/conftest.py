import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FS
from webdriver_manager.firefox import GeckoDriverManager
from Diplom_3.fixtures.api_methods import generate_user_credentials, register_user as api_register_user
from Diplom_3.pages.feed_page import FeedPage
from Diplom_3.pages.main_page import MainPage
from Diplom_3.pages.login_page import LoginPage
from Diplom_3.pages.reset_password_page import ResetPasswordPage
from Diplom_3.urls import URL_HOME, URL_LOGIN, URL_RESET_PASSWORD, URL_FORGOT_PASSWORD, URL_ORDERS_FEED


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):

    if request.param == 'firefox':
        firefox_driver = GeckoDriverManager().install()
        service = FS(firefox_driver)
        driver = webdriver.Firefox(service=service)
    else:
        driver = webdriver.Chrome()
    yield driver
    driver.quit()


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


@pytest.fixture()
def register_user(driver):
    """
    Генерирует учетные данные пользователя и регистрирует его через API.
    Возвращает словарь с учетными данными.
    """
    credentials = generate_user_credentials()
    api_register_user(credentials)
    return {
        'credentials': credentials
    }


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
