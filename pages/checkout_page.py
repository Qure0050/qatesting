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
        self.driver.execute_script("arguments[0].click();", btn)

    def fill_customer_info(self, first, last, postal):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))
        if first:
            self.type_text(self.FIRST_NAME, first)
        if last:
            self.type_text(self.LAST_NAME, last)
        if postal:
            self.type_text(self.POSTAL_CODE, postal)
        btn = self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTN))
        self.driver.execute_script("arguments[0].click();", btn)

    def finish_checkout(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.FINISH_BTN))
        self.driver.execute_script("arguments[0].click();", btn)

    def get_confirmation_text(self):
        return self.get_text(self.COMPLETE_HEADER)

    def get_error_text(self):
        return self.get_text(self.ERROR_BANNER)