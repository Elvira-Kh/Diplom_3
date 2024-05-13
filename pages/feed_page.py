import allure
from Diplom_3.locators.feed_page_locators import FeedPageLocators
from Diplom_3.pages.base_page import BasePage


class FeedPage(BasePage):

    @allure.step('Найти ссылку на "Конструктор"')
    def get_constructor_link(self):
        return self.find_element(FeedPageLocators.LINK_CONSTRUCTOR)

    @allure.step('Найти ссылку на "Восстановить пароль"')
    def get_orders_feed_link(self):
        return self.find_element(FeedPageLocators.LINK_ORDERS_FEED)

    @allure.step('Найти заголовок "Лента заказов"')
    def get_orders_feed_title(self):
        return self.find_element(FeedPageLocators.HEADING_ORDERS_FEED)

    @allure.step('Найти ссылку на первый заказ')
    def get_first_order_link(self):
        return self.find_element(FeedPageLocators.LINK_FIRST_ORDER)

    @allure.step('Получить список номеров заказов из ленты')
    def get_orders_ids(self):
        orders = self.find_elements(FeedPageLocators.TEXT_ORDER_ID)
        return [order.text.lstrip('#').lstrip('0') for order in orders]

    @allure.step('Получить список номеров заказов из "В работе"')
    def get_in_work_orders_ids(self):
        orders = self.find_elements(FeedPageLocators.TEXT_ORDER_ID_IN_WORK)
        return [order.text.lstrip('#').lstrip('0') for order in orders]
