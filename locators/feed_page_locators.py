from selenium.webdriver.common.by import By


class FeedPageLocators:
    LINK_CONSTRUCTOR = (By.XPATH, './/a[@href="/"]')
    LINK_ORDERS_FEED = (By.XPATH, './/a[@href="/feed"]')
    HEADING_ORDERS_FEED = (By.XPATH, './/h1')
    TEXT_TITLE_DONE_BY_ALL_TIME = (By.XPATH, './/p[text()="Выполнено за все время:"]')
    TEXT_COUNTER_DONE_BY_ALL_TIME = (By.XPATH, '(.//p[contains(@class,"OrderFeed_number")])[1]')
    TEXT_TITLE_DONE_BY_TODAY = (By.XPATH, './/p[text()="Выполнено за сегодня:"]')
    TEXT_COUNTER_DONE_BY_TODAY = (By.XPATH, '(.//p[contains(@class,"OrderFeed_number")])[2]')
    LINK_FIRST_ORDER = (By.XPATH, './/a[contains(@class,"OrderHistory_link")]')
    DIV_MODAL_CONTAINER = (
        By.XPATH,
        './/section[contains(@class,"opened")]/div[contains(@class,"Modal_modal__container")]'
    )
    BUTTON_MODAL_CLOSE = (
        By.XPATH,
        './/section[contains(@class,"opened")]/div/button[contains(@class,"Modal_modal__close_modified")]'
    )
    TEXT_ORDER_ID = (By.XPATH, './/a/div/p[contains(@class,"text_type_digits-default")]')
    TEXT_ORDER_ID_IN_WORK = (By.XPATH, './/ul[contains(@class,"OrderFeed_orderListReady")]/li')
