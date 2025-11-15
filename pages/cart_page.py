from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.cart_item_count_locator = (
            By.CSS_SELECTOR, ".cart-page__title--append")

    def get_cart_items_count(self):
        """Возвращает количество товаров в корзине"""
        count_element = self.wait.until(
            EC.visibility_of_element_located(self.cart_item_count_locator)
        )
        count_text = count_element.text.strip()

        match = re.search(r'\d+', count_text)
        if match:
            count = int(match.group())
            return count
        else:
            return 0
