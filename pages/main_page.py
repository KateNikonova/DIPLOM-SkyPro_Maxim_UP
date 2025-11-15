from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from constants import MAIN_PAGE_URL


class MainPage:
    def __init__(self, driver):
        """Главная страница.
        """
        self.driver = driver
        self.url = MAIN_PAGE_URL
        self.wait = WebDriverWait(driver, 10)
        self.popup_locator = (By.CSS_SELECTOR, ".tippy-box")
        self.close_button_locator = (By.CSS_SELECTOR, ".chg-app-button")
        self.buy_button_locator = (By.CSS_SELECTOR, ".chg-app-button__content")
        self.search_input_locator = (By.CSS_SELECTOR, "input.search-form__input")
        self.search_results_locator = (By.CSS_SELECTOR, ".product-card, .search-results")

    def open(self):
        """Открывает главную страницу и закрывает всплывающее окно."""
        self.driver.get(self.url)
        self._close_popup()

    def _close_popup(self):
        """Закрывает всплывающее окно, если оно появилось.
        """
        try:
            popup = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(self.popup_locator)
            )
            popup.find_element(*self.close_button_locator).click()
        except Exception:
            pass

    def _find(self, locator):
        """Находит элемент на странице с ожиданием.
        """
        return self.wait.until(EC.visibility_of_element_located(locator))

    def search(self, text):
        """Выполняет поиск по сайту.
        """
        search_field = self._find(self.search_input_locator)
        search_field.clear()
        search_field.send_keys(text)
        search_field.send_keys(Keys.ENTER)

    def wait_for_search_results(self):
        """Ожидает появления результатов поиска на странице."""
        self.wait.until(EC.presence_of_element_located(self.search_results_locator))

    def get_results_count(self):
        """Возвращает количество найденных товаров.
        """
        results = self.driver.find_elements(*self.search_results_locator)
        return len(results)