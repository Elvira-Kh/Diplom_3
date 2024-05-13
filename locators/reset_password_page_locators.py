from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    INPUT_EMAIL = (By.XPATH, './/input[@name="name"]')
    BUTTON_RECOVER = (By.XPATH, './/form/button')
    DIV_HIDE_SHOW_PASSWORD = (By.XPATH, './/div[@class="input__icon input__icon-action"]')
    INPUT_PASSWORD = (By.XPATH, './/input[@name="Введите новый пароль"]')
