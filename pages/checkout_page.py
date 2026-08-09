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

    def fill_customer_info(self, first, last, postal):
        # Advanced QA technique: Force Selenium to wait for React to register the text
        def safe_enter(locator, text):
            field = self.wait.until(EC.element_to_be_clickable(locator))
            field.click()
            field.clear()
            field.send_keys(text)
            # Halt execution until the DOM 'value' attribute physically matches the text
            WebDriverWait(self.driver, 5).until(
                lambda d: d.find_element(*locator).get_attribute("value") == text
            )

        # Only interact with fields if data was passed in the test
        if first:
            safe_enter(self.FIRST_NAME, first)
        if last:
            safe_enter(self.LAST_NAME, last)
        if postal:
            safe_enter(self.POSTAL_CODE, postal)
        
        # Now it is 100% safe to click continue
        btn = self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTN))
        btn.click()

    def finish_checkout(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.FINISH_BTN))
        btn.click()

    def get_confirmation_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER)).text

    def get_error_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_BANNER)).text