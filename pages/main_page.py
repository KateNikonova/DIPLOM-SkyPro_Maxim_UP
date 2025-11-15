from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.popup_locator = (By.CSS_SELECTOR, ".tippy-box")
        self.close_button_locator = (By.CSS_SELECTOR, ".chg-app-button")
        self.search_input_locator = (
            By.CSS_SELECTOR, "input.search-form__input")
        self.search_suggest_locator = (
            By.CSS_SELECTOR, ".suggests-list__link")

    def open(self):
        """Открывает главную страницу и закрывает всплывающее окно"""
        self.driver.get("https://www.chitai-gorod.ru/")
        self._close_popup()

    def _close_popup(self):
        """Закрывает всплывающее окно"""
        popup = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.popup_locator)
        )
        popup.find_element(*self.close_button_locator).click()

    def search(self, text):
        """Выполняет поиск по сайту"""
        search_field = self.wait.until(
            EC.visibility_of_element_located(
                self.search_input_locator))
        search_field.clear()
        search_field.send_keys(text)

        first_suggest = self.wait.until(
            EC.element_to_be_clickable(self.search_suggest_locator)
        )
        first_suggest.click()
