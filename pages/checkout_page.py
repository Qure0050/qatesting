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
        btn = self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BTN))
        btn.click()
        time.sleep(1)

    def fill_customer_info(self, first, last, postal):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))
        
        # Click, clear, and type for EVERY field so React registers the event
        first_field = self.driver.find_element(*self.FIRST_NAME)
        first_field.click()
        first_field.clear()
        first_field.send_keys(first)
        
        last_field = self.driver.find_element(*self.LAST_NAME)
        last_field.click()
        last_field.clear()
        last_field.send_keys(last)
        
        postal_field = self.driver.find_element(*self.POSTAL_CODE)
        postal_field.click()
        postal_field.clear()
        postal_field.send_keys(postal)
        
        time.sleep(1) # Absolute pause to let React save the state
        
        # NATIVE click (no execute_script) so the text box loses focus properly
        continue_btn = self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTN))
        continue_btn.click()
        time.sleep(1)

    def finish_checkout(self):
        finish_btn = self.wait.until(EC.element_to_be_clickable(self.FINISH_BTN))
        finish_btn.click()
        time.sleep(1)

    def get_confirmation_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER)).text

    def get_error_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_BANNER)).text