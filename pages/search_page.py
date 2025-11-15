from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.search_results_locator = (By.CSS_SELECTOR, ".product-card")
        self.buy_button_locator = (
            By.CSS_SELECTOR,
            "button.product-buttons__main-action")
        self.cart_button_locator = (
            By.XPATH, "//button[contains(., 'Корзина')]")

    def wait_for_search_results(self):
        self.wait.until(
            EC.presence_of_element_located(
                self.search_results_locator))

    def get_results_count(self):
        results = self.driver.find_elements(*self.search_results_locator)
        return len(results)

    def add_first_product_to_cart(self):
        buy_buttons = self.wait.until(
            EC.presence_of_all_elements_located(self.buy_button_locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            buy_buttons[0])
        self.driver.execute_script("arguments[0].click();", buy_buttons[0])

    def go_to_cart(self):
        cart_button = self.wait.until(
            EC.element_to_be_clickable(self.cart_button_locator)
        )
        cart_button.click()
