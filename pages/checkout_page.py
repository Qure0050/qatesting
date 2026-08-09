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
        btn = self.wait.until(EC.presence_of_element_located(self.CHECKOUT_BTN))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", btn)
        time.sleep(1)

    def fill_customer_info(self, first, last, postal):
        self.wait.until(EC.presence_of_element_located(self.FIRST_NAME))
        if first:
            self.driver.find_element(*self.FIRST_NAME).send_keys(first)
        if last:
            self.driver.find_element(*self.LAST_NAME).send_keys(last)
        if postal:
            self.driver.find_element(*self.POSTAL_CODE).send_keys(postal)
        
        time.sleep(0.5)
        btn = self.driver.find_element(*self.CONTINUE_BTN)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        self.driver.execute_script("arguments[0].click();", btn)
        time.sleep(1)

    def finish_checkout(self):
        btn = self.wait.until(EC.presence_of_element_located(self.FINISH_BTN))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        self.driver.execute_script("arguments[0].click();", btn)
        time.sleep(1)

    def get_confirmation_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER)).text

    def get_error_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_BANNER)).text