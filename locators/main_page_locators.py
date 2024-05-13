from selenium.webdriver.common.by import By


class MainPageLocators:
    LINK_CONSTRUCTOR = (By.XPATH, './/a[@href="/"]')
    LINK_ORDERS_FEED = (By.XPATH, './/a[@href="/feed"]')
    LINK_ACCOUNT = (By.XPATH, './/a[@href="/account"]')
    LINK_INGREDIENT_1 = (By.XPATH, '(.//div[contains(@class,"BurgerIngredient_ingredient")])[1]')
    TEXT_INGREDIENT_1_COUNTER = (By.XPATH, '(.//p[contains(@class,"counter_counter__num")])[1]')
    DIV_INGREDIENT_TOP_SLOT = (By.XPATH, './/div[contains(@class,"constructor-element constructor-element_pos_top")]')
    DIV_MODAL_CONTAINER = (By.XPATH, './/div[contains(@class,"Modal_modal__container")]')
    BUTTON_MODAL_CLOSE = (By.XPATH, './/button[contains(@class,"Modal_modal__close_modified")]')
    TEXT_MODAL_ORDER_NUMBER = (By.XPATH, './/div[contains(@class,"Modal_modal__contentBox")]/h2')
    BUTTON_CREATE_ORDER = (By.XPATH, './/button[text()="Оформить заказ"]')
    TEXT_ORDER_ID_SUBTITLE = (By.XPATH, './/p[text()="идентификатор заказа"]')
