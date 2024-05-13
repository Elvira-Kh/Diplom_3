import allure
from Diplom_3.locators.account_page_locators import AccountPageLocators
from Diplom_3.pages.base_page import BasePage


class AccountPage(BasePage):

    @allure.step('Найти поле ввода "Имя"')
    def get_name_input(self):
        return self.find_element(AccountPageLocators.INPUT_NAME)

    @allure.step('Найти поле ввода "Email"')
    def get_email_input(self):
        return self.find_element(AccountPageLocators.INPUT_EMAIL)

    @allure.step('Найти поле ввода "Пароль"')
    def get_password_input(self):
        return self.find_element(AccountPageLocators.INPUT_PASSWORD)

    @allure.step('Найти ссылку "История заказов"')
    def get_orders_history_link(self):
        return self.find_element(AccountPageLocators.LINK_ORDERS_HISTORY)

    @allure.step('Найти ссылку "Лента заказов"')
    def get_orders_feed_link(self):
        return self.find_element(AccountPageLocators.LINK_ORDERS_FEED)

    @allure.step('Найти кнопку "Выход"')
    def get_exit_button(self):
        return self.find_element(AccountPageLocators.BUTTON_EXIT)

    @allure.step('Получить список номеров заказов в "История заказов"')
    def get_orders_ids(self):
        orders = self.find_elements(AccountPageLocators.TEXT_ORDER_ID)
        return [order.text.lstrip('#').lstrip('0') for order in orders]
