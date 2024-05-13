from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_EMAIL = (By.XPATH, './/input[@name="name"]')
    INPUT_PASSWORD = (By.XPATH, './/input[@name="Пароль"]')
    BUTTON_ENTER = (By.XPATH, './/form/button')
    LINK_FORGOT_PASSWORD = (By.XPATH, './/a[@href="/forgot-password"]')
