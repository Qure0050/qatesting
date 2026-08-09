import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    CHECKOUT_BTN = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    ERROR_BANNER = (By.CSS_SELECTOR, "h3[data-test='error']")

    def start_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BTN)).click()
        time.sleep(1)  # Force sync for CI runners

    def fill_customer_info(self, first, last, postal):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))
        
        if first:
            self.driver.find_element(*self.FIRST_NAME).send_keys(first)
        if last:
            self.driver.find_element(*self.LAST_NAME).send_keys(last)
        if postal:
            self.driver.find_element(*self.POSTAL_CODE).send_keys(postal)
        
        time.sleep(0.5)  # Let React register the typed text
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTN)).click()
        time.sleep(1)  # Wait for next page to load

    def finish_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BTN)).click()
        time.sleep(1)  # Wait for confirmation page

    def get_confirmation_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER)).text

    def get_error_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_BANNER)).text