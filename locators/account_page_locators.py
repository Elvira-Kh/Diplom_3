from selenium.webdriver.common.by import By


class AccountPageLocators:
    INPUT_NAME = (By.XPATH, './/input[@name="Name"]')
    INPUT_EMAIL = (By.XPATH, './/input[@name="name" and @type="text"]')
    INPUT_PASSWORD = (By.XPATH, './/input[@name="name" and @type="password"]')
    LINK_ORDERS_HISTORY = (By.XPATH, './/a[@href="/account/order-history"]')
    BUTTON_EXIT = (By.XPATH, './/button[text()="Выход"]')
    LINK_ORDERS_FEED = (By.XPATH, './/a[@href="/feed"]')
    LIST_ORDERS_HISTORY = (By.XPATH, './/ul[contains(@class,"OrderHistory_profileList")]')
    TEXT_ORDER_ID = (By.XPATH, './/a/div/p[contains(@class,"text_type_digits-default")]')
