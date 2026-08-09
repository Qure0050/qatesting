from selenium.webdriver.common.by import By
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
        self.click(self.CHECKOUT_BTN)

    def fill_customer_info(self, first, last, postal):
        if first:
            self.type_text(self.FIRST_NAME, first)
        if last:
            self.type_text(self.LAST_NAME, last)
        if postal:
            self.type_text(self.POSTAL_CODE, postal)
        self.click(self.CONTINUE_BTN)

    def finish_checkout(self):
        self.click(self.FINISH_BTN)

    def get_confirmation_text(self):
        return self.get_text(self.COMPLETE_HEADER)

    def get_error_text(self):
        return self.get_text(self.ERROR_BANNER)