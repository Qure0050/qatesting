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
        # Ensure routing to checkout step one is complete
        self.wait.until(EC.url_contains("checkout-step-one"))

    def fill_customer_info(self, first, last, postal):
        def type_field(locator, text):
            field = self.wait.until(EC.element_to_be_clickable(locator))
            field.click()
            field.clear()
            if text:
                field.send_keys(text)

        type_field(self.FIRST_NAME, first)
        type_field(self.LAST_NAME, last)
        type_field(self.POSTAL_CODE, postal)
        
        btn = self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTN))
        btn.click()

    def finish_checkout(self):
        # Ensure routing to checkout step two is complete before looking for finish
        self.wait.until(EC.url_contains("checkout-step-two"))
        btn = self.wait.until(EC.element_to_be_clickable(self.FINISH_BTN))
        btn.click()

    def get_confirmation_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER)).text

    def get_error_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_BANNER)).text