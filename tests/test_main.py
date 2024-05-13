import allure
from Diplom_3.locators.feed_page_locators import FeedPageLocators
from Diplom_3.locators.main_page_locators import MainPageLocators
from Diplom_3.pages.feed_page import FeedPage
from Diplom_3.fixtures.conftest import main_page, authorize_user, driver, register_user, login_page
from Diplom_3.urls import URL_HOME, URL_ORDERS_FEED


class TestMainFunctional:

    @allure.title('Переход по клику на "Конструктор" открывает страницу с конструктором')
    @allure.description('Переход по клику на "Конструктор" открывает страницу с конструктором')
    def test_click_by_constructor_opens_the_constructor_page(self, main_page):
        main_page.get_constructor_link().click()
        main_page.wait_for_url(5, URL_HOME)
        assert main_page.get_current_url() == URL_HOME
        assert main_page.get_constructor_link().get_attribute('class').find('AppHeader_header__link_active') != -1

    @allure.title('Переход по клику на "Лента заказов" открывает страницу с лентой заказов')
    @allure.description('Переход по клику на "Лента заказов" открывает страницу с лентой заказов')
    def test_click_by_orders_feed_opens_the_orders_feed_page(self, main_page):
        main_page.get_orders_feed_link().click()
        main_page.wait_for_url(5, URL_ORDERS_FEED)
        assert main_page.get_current_url() == URL_ORDERS_FEED
        feed_page = FeedPage(main_page.get_driver())
        assert feed_page.get_orders_feed_link().get_attribute('class').find('AppHeader_header__link_active') != -1
        assert feed_page.is_visible(5, FeedPageLocators.HEADING_ORDERS_FEED)
        assert feed_page.is_visible(5, FeedPageLocators.TEXT_TITLE_DONE_BY_ALL_TIME)
        assert feed_page.is_visible(5, FeedPageLocators.TEXT_TITLE_DONE_BY_TODAY)

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @allure.description('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_by_ingredient_opens_the_ingredient_details(self, main_page):
        main_page.get_first_ingredient_link().click()
        assert main_page.is_visible(5, MainPageLocators.DIV_MODAL_CONTAINER)

    @allure.title('Если кликнуть на крестик окна с деталями, тогда окно закроется')
    @allure.description('Если кликнуть на крестик окна с деталями, тогда окно закроется')
    def test_click_by_ingredient_details_cross_closes_the_ingredient_details(self, main_page):
        main_page.get_first_ingredient_link().click()
        assert main_page.is_visible(5, MainPageLocators.DIV_MODAL_CONTAINER)
        assert main_page.is_visible(5, MainPageLocators.BUTTON_MODAL_CLOSE)
        main_page.get_modal_close_button().click()
        assert main_page.is_invisible(5, MainPageLocators.DIV_MODAL_CONTAINER)

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    @allure.description('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_add_ingredient_increments_the_ingredient_counter(self, main_page):
        assert main_page.is_visible(5, MainPageLocators.LINK_INGREDIENT_1)
        assert main_page.is_visible(5, MainPageLocators.TEXT_INGREDIENT_1_COUNTER)
        assert main_page.get_first_ingredient_counter().text == "0"
        main_page.drag_and_drop_first_ingredient_onto_top_slot()
        main_page.wait_for_text_not_equals(5, MainPageLocators.TEXT_INGREDIENT_1_COUNTER, "0")
        assert main_page.get_first_ingredient_counter().text == "2"

    @allure.title('Авторизованный пользователь может оформить заказ')
    @allure.description('Авторизованный пользователь может оформить заказ')
    def test_authorized_user_allowed_to_create_order(self, authorize_user):
        main_page = authorize_user['main_page']
        assert main_page.is_visible(5, MainPageLocators.BUTTON_CREATE_ORDER)
        main_page.get_create_order_button().click()
        assert main_page.is_visible(5, MainPageLocators.DIV_MODAL_CONTAINER)
        assert main_page.is_visible(5, MainPageLocators.TEXT_ORDER_ID_SUBTITLE)
