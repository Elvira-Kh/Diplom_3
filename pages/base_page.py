import time

import allure
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait, POLL_FREQUENCY


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_driver(self):
        return self.driver

    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ищем элемент на странице')
    def find_element(self, locator):
        element = self.driver.find_element(*locator)
        original_click = element.click
        element.click = lambda: self.patched_click(element, original_click)
        return element

    @allure.step('Ищем элементы на странице')
    def find_elements(self, locator):
        elements = self.driver.find_elements(*locator)
        for element in elements:
            original_click = element.click
            element.click = lambda: self.patched_click(element, original_click)
        return elements

    @allure.step('Проверяем, станет ли элемент видимым за отведённое время')
    def is_visible(self, timeout, locator):
        end_time = time.monotonic() + timeout
        while True:
            try:
                element = self.driver.find_element(*locator)
                if element.is_displayed():
                    return True
            except NoSuchElementException:
                pass
            time.sleep(POLL_FREQUENCY)
            if time.monotonic() > end_time:
                return False

    @allure.step('Проверяем, исчезнет ли заданный текст за отведённое время')
    def wait_for_text_not_equals(self, timeout, locator, text):
        end_time = time.monotonic() + timeout
        while True:
            try:
                element = self.driver.find_element(*locator)
                if element.is_displayed() and element.text != text:
                    return element.text
            except NoSuchElementException:
                pass
            time.sleep(POLL_FREQUENCY)
            if time.monotonic() > end_time:
                return None

    @allure.step('Проверяем, станет ли элемент невидимым за отведённое время')
    def is_invisible(self, timeout, locator):
        end_time = time.monotonic() + timeout
        while True:
            try:
                element = self.driver.find_element(*locator)
                if not element.is_displayed():
                    return True
            except NoSuchElementException:
                return True
            time.sleep(POLL_FREQUENCY)
            if time.monotonic() > end_time:
                return False

    @allure.step('Ожидаем, пока элемент не станет видимым')
    def wait_until_visible(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидаем, пока не загрузится URL')
    def wait_for_url(self, timeout, url):
        WebDriverWait(self.driver, timeout).until(expected_conditions.url_to_be(url))

    @allure.step('Получаем активный элемент')
    def get_active_element(self):
        return self.driver.switch_to.active_element

    @allure.step('Перетаскиваем элемент')
    def drag_and_drop(self, drag_element, drop_element):
        ActionChains(self.driver).drag_and_drop(drag_element, drop_element).perform()

    def patched_click(self, element, original_click):
        try:
            original_click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)
