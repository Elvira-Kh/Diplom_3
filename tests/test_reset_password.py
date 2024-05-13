import allure
from Diplom_3.pages.reset_password_page import ResetPasswordPage
from Diplom_3.fixtures.conftest import main_page, authorize_user, driver, register_user, login_page, feed_page, reset_password_page
from Diplom_3.urls import URL_FORGOT_PASSWORD, URL_RESET_PASSWORD


class TestRecoverPassword:

    @allure.title('Проверка, что кнопка "Восстановить пароль" открывает страницу восстановления пароля')
    @allure.description('Проверка, что кнопка "Восстановить пароль" открывает страницу восстановления пароля')
    def test_click_by_recover_password_button_opens_the_forgot_password_page(self, login_page):
        login_page.get_forgot_password_link().click()
        login_page.wait_for_url(5, URL_FORGOT_PASSWORD)
        assert login_page.get_current_url() == URL_FORGOT_PASSWORD

    @allure.title('Проверка, что кнопка "Восстановить" открывает страницу ввода нового пароля')
    @allure.description('Проверка, что кнопка "Восстановить" открывает страницу ввода нового пароля')
    def test_enter_email_and_click_by_recover_button_opens_the_reset_password_page(self, reset_password_page):
        reset_password_page.get_email_input().send_keys('test@mail.ru')
        reset_password_page.get_recover_button().click()
        reset_password_page.wait_for_url(5, URL_RESET_PASSWORD)
        assert reset_password_page.get_current_url() == URL_RESET_PASSWORD

    @allure.title('Проверка, что клик по иконке "Показать/Скрыть пароль" активирует поле ввода пароля')
    @allure.description('Проверка, что клик по иконке "Показать/Скрыть пароль" активирует поле ввода пароля')
    def test_click_by_show_or_hide_password_activates_the_password_field(self, reset_password_page):
        reset_password_page.get_email_input().send_keys('test@mail.ru')
        reset_password_page.get_recover_button().click()
        reset_password_page.wait_for_url(5, URL_RESET_PASSWORD)
        reset_password_page = ResetPasswordPage(reset_password_page.driver)
        hide_show_password_icon = reset_password_page.get_hide_show_password_icon()
        password_input = reset_password_page.get_password_input()
        password_input.send_keys('password')
        hide_show_password_icon.click()
        assert password_input == reset_password_page.get_active_element()
        hide_show_password_icon.click()
        assert password_input == reset_password_page.get_active_element()
