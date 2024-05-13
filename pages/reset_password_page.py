import allure
from Diplom_3.locators.reset_password_page_locators import ResetPasswordPageLocators
from Diplom_3.pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    @allure.step('Найти поле ввода "Email"')
    def get_email_input(self):
        return self.find_element(ResetPasswordPageLocators.INPUT_EMAIL)

    @allure.step('Найти кнопку "Восстановить"')
    def get_recover_button(self):
        return self.find_element(ResetPasswordPageLocators.BUTTON_RECOVER)

    @allure.step('Найти иконку "Скрыть/Показать пароль"')
    def get_hide_show_password_icon(self):
        return self.find_element(ResetPasswordPageLocators.DIV_HIDE_SHOW_PASSWORD)

    @allure.step('Найти поле ввода "Пароль"')
    def get_password_input(self):
        return self.find_element(ResetPasswordPageLocators.INPUT_PASSWORD)
