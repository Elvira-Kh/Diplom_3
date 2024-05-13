import allure
from Diplom_3.pages.account_page import AccountPage
from Diplom_3.fixtures import URL_LOGIN, URL_ACCOUNT_PROFILE, URL_ACCOUNT_ORDERS_HISTORY


class TestAccount:

    @allure.title('Кнопка "Личный Кабинет" открывает стр. авторизации для неавторизованного пользователя')
    @allure.description('Кнопка "Личный Кабинет" открывает стр. авторизации для неавторизованного пользователя')
    def test_not_authorized_click_by_profile_opens_the_account_page(self, main_page):
        main_page.get_account_link().click()
        main_page.wait_for_url(5, URL_LOGIN)
        assert main_page.get_current_url() == URL_LOGIN

    @allure.title('Кнопка "Личный Кабинет" открывает стр. профиля для авторизованного пользователя')
    @allure.description('Кнопка "Личный Кабинет" открывает стр. профиля для авторизованного пользователя')
    def test_authorized_click_by_profile_opens_the_account_page(self, authorize_user):
        credentials = authorize_user['credentials']
        main_page = authorize_user['main_page']
        # Делаем клик по "Личный Кабинет"
        main_page.get_account_link().click()
        main_page.wait_for_url(5, URL_ACCOUNT_PROFILE)
        assert main_page.get_current_url() == URL_ACCOUNT_PROFILE
        account_page = AccountPage(main_page.get_driver())
        assert account_page.get_name_input().get_property('value') == credentials['name']
        assert account_page.get_email_input().get_property('value') == credentials['email']

    @allure.title('Кнопка "История заказов" открывает страницу истории заказов')
    @allure.description('Кнопка "История заказов" открывает страницу истории заказов')
    def test_click_by_orders_history_opens_the_orders_history_page(self, authorize_user):
        main_page = authorize_user['main_page']
        # Делаем клик по "Личный Кабинет"
        main_page.get_account_link().click()
        main_page.wait_for_url(5, URL_ACCOUNT_PROFILE)
        # Делаем клик по "История заказов"
        account_page = AccountPage(main_page.get_driver())
        account_page.get_orders_history_link().click()
        account_page.wait_for_url(5, URL_ACCOUNT_ORDERS_HISTORY)
        assert account_page.get_current_url() == URL_ACCOUNT_ORDERS_HISTORY
        assert account_page.get_orders_history_link().get_attribute('class').find('Account_link_active') != -1

    @allure.title('Кнопка "Выход" открывает страницу авторизации')
    @allure.description('Кнопка "Выход" открывает страницу авторизации')
    def test_click_by_exit_opens_the_login_page(self, authorize_user):
        main_page = authorize_user['main_page']
        # Делаем клик по "Личный Кабинет"
        main_page.get_account_link().click()
        main_page.wait_for_url(5, URL_ACCOUNT_PROFILE)
        # Делаем клик по "Выход"
        account_page = AccountPage(main_page.get_driver())
        account_page.get_exit_button().click()
        account_page.wait_for_url(5, URL_LOGIN)
        assert account_page.get_current_url() == URL_LOGIN