import allure
from Diplom_3.locators.login_page_locators import LoginPageLocators
from Diplom_3.pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Найти поле ввода "Email"')
    def get_email_input(self):
        return self.find_element(LoginPageLocators.INPUT_EMAIL)

    @allure.step('Найти поле ввода "Пароль"')
    def get_password_input(self):
        return self.find_element(LoginPageLocators.INPUT_PASSWORD)

    @allure.step('Найти кнопку "Войти"')
    def get_enter_button(self):
        return self.find_element(LoginPageLocators.BUTTON_ENTER)

    @allure.step('Найти ссылку на "Восстановить пароль"')
    def get_forgot_password_link(self):
        return self.find_element(LoginPageLocators.LINK_FORGOT_PASSWORD)
