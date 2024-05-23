import allure
import pytest

from Diplom_3.locators import AccountPageLocators
from Diplom_3.locators import FeedPageLocators
from Diplom_3.pages.feed_page import FeedPage
from Diplom_3.pages.account_page import AccountPage
from Diplom_3.pages.main_page import MainPage
from Diplom_3.fixtures import URL_HOME, URL_ACCOUNT_PROFILE, URL_ACCOUNT_ORDERS_HISTORY, URL_ORDERS_FEED


class TestOrdersFeed:

    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.description('Тест проверяет открытие всплывающего окна при клике на заказ')
    def test_click_by_order_opens_the_order_details(self, feed_page):
        feed_page.get_first_order_link().click()
        assert feed_page.is_visible(5, FeedPageLocators.DIV_MODAL_CONTAINER), "Отсутствует всплывающее окно"
        assert feed_page.is_visible(5, FeedPageLocators.BUTTON_MODAL_CLOSE), "Кнопка закрытия не найдена"

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.description('Тест проверяет отображение заказов из истории заказов на странице Лента заказов')
    def test_orders_from_orders_history_presented_in_the_orders_feed(self, authorize_user):
        credentials = authorize_user['credentials']
        main_page = authorize_user['main_page']
        main_page.create_order(credentials)
        main_page.get_account_link().click()
        main_page.wait_for_url(5, URL_ACCOUNT_PROFILE)
        account_page = AccountPage(main_page.get_driver())
        account_page.get_orders_history_link().click()
        account_page.wait_for_url(5, URL_ACCOUNT_ORDERS_HISTORY)
        account_page.wait_until_visible(5, AccountPageLocators.TEXT_ORDER_ID)
        history_orders_ids = account_page.get_orders_ids()
        assert history_orders_ids, "История заказов пуста"

        account_page.get_orders_feed_link().click()
        account_page.wait_for_url(5, URL_ORDERS_FEED)
        orders_feed = FeedPage(account_page.get_driver())
        feed_orders_ids = orders_feed.get_orders_ids()
        assert set(history_orders_ids) == set(feed_orders_ids), "Списки заказов не совпадают"

    @allure.title('При создании нового заказа счётчик "Выполнено за всё_время/сегодня" увеличивается')
    @allure.description('Тест проверяет увеличение счётчика при создании нового заказа')
    @pytest.mark.parametrize(
        'locator',
        [
            FeedPageLocators.TEXT_COUNTER_DONE_BY_ALL_TIME,
            FeedPageLocators.TEXT_COUNTER_DONE_BY_TODAY,
        ]
    )
    def test_create_new_order_updates_done_by_all_time_counter(self, authorize_user, locator):
        credentials = authorize_user['credentials']
        main_page = authorize_user['main_page']
        main_page.get_orders_feed_link().click()
        main_page.wait_for_url(5, URL_ORDERS_FEED)
        feed_page = FeedPage(main_page.get_driver())
        feed_page.wait_until_visible(5, locator)
        counter_before = feed_page.find_element(locator).text

        feed_page.get_constructor_link().click()
        feed_page.wait_for_url(5, URL_HOME)
        main_page = MainPage(feed_page.get_driver())
        main_page.create_order(credentials)

        main_page.get_orders_feed_link().click()
        main_page.wait_for_url(5, URL_ORDERS_FEED)
        feed_page = FeedPage(main_page.get_driver())
        feed_page.wait_for_text_not_equals(5, locator, counter_before)
        counter_after = feed_page.find_element(locator).text

        assert int(counter_before) < int(counter_after), "Счётчик не увеличился после создания заказа"

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    @allure.description('Тест проверяет появление номера заказа в списке заказов в работе')
    def test_create_new_order_updates_list_of_in_work_orders(self, authorize_user):
        credentials = authorize_user['credentials']
        main_page = authorize_user['main_page']
        order_id = main_page.create_order(credentials)['order_id']

        main_page.get_orders_feed_link().click()
        main_page.wait_for_url(5, URL_ORDERS_FEED)
        feed_page = FeedPage(main_page.get_driver())
        feed_page.wait_for_text_not_equals(5, FeedPageLocators.TEXT_ORDER_ID_IN_WORK, "Все текущие заказы готовы!")
        order_ids = feed_page.get_in_work_orders_ids()
        assert order_ids, "Список заказов в работе пуст"
        assert order_id in order_ids, f"Заказ с номером {order_id} не найден в списке заказов в работе"
