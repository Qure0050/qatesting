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
        btn = self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BTN))
        btn.click()
        self.wait.until(EC.url_contains("checkout-step-one.html"))

    def fill_customer_info(self, first, last, postal):
        if first:
            field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME))
            field.click()
            field.clear()
            field.send_keys(first)
        if last:
            field = self.wait.until(EC.element_to_be_clickable(self.LAST_NAME))
            field.click()
            field.clear()
            field.send_keys(last)
        if postal:
            field = self.wait.until(EC.element_to_be_clickable(self.POSTAL_CODE))
            field.click()
            field.clear()
            field.send_keys(postal)
        
        continue_btn = self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTN))
        continue_btn.click()

    def finish_checkout(self):
        self.wait.until(EC.url_contains("checkout-step-two.html"))
        finish_btn = self.wait.until(EC.element_to_be_clickable(self.FINISH_BTN))
        finish_btn.click()

    def get_confirmation_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER)).text

    def get_error_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_BANNER)).text