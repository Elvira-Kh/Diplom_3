import allure
from Diplom_3.locators.main_page_locators import MainPageLocators
from Diplom_3.pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Найти ссылку на "Конструктор"')
    def get_constructor_link(self):
        return self.find_element(MainPageLocators.LINK_CONSTRUCTOR)

    @allure.step('Найти ссылку на "Лента заказов"')
    def get_orders_feed_link(self):
        return self.find_element(MainPageLocators.LINK_ORDERS_FEED)

    @allure.step('Найти ссылку на "Личный Кабинет"')
    def get_account_link(self):
        return self.find_element(MainPageLocators.LINK_ACCOUNT)

    @allure.step('Найти ссылку на первый ингредиент')
    def get_first_ingredient_link(self):
        return self.find_element(MainPageLocators.LINK_INGREDIENT_1)

    @allure.step('Найти счётчик первого ингредиента')
    def get_first_ingredient_counter(self):
        return self.find_element(MainPageLocators.TEXT_INGREDIENT_1_COUNTER)

    @allure.step('Найти модальный контейнер')
    def get_modal_container(self):
        return self.find_element(MainPageLocators.DIV_MODAL_CONTAINER)

    @allure.step('Найти кнопку для закрытия модального окна')
    def get_modal_close_button(self):
        return self.find_element(MainPageLocators.BUTTON_MODAL_CLOSE)

    @allure.step('Найти текст с номером заказа в модальном окне')
    def get_modal_order_number_text(self):
        return self.find_element(MainPageLocators.TEXT_MODAL_ORDER_NUMBER)

    @allure.step('Найти кнопку для создания заказа')
    def get_create_order_button(self):
        return self.find_element(MainPageLocators.BUTTON_CREATE_ORDER)

    @allure.step('Перетащить первый ингредиент на верхний слот ингредиентов')
    def drag_and_drop_first_ingredient_onto_top_slot(self):
        ingredient = self.get_first_ingredient_link()
        top_slot = self.find_element(MainPageLocators.DIV_INGREDIENT_TOP_SLOT)
        self.drag_and_drop(ingredient, top_slot)

    @allure.step('Создаём заказ')
    def create_order(self, credentials):
        self.drag_and_drop_first_ingredient_onto_top_slot()
        self.get_create_order_button().click()
        order_id = self.wait_for_text_not_equals(15, MainPageLocators.TEXT_MODAL_ORDER_NUMBER, '9999')
        self.get_modal_close_button().click()
        return {
            'credentials': credentials,
            'order_id': order_id
        }
