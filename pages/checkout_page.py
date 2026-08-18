from selenium.webdriver.common.by import By
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

    def _js_click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def start_checkout(self):
        self._js_click(self.CHECKOUT_BTN)
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))

    def fill_customer_info(self, first, last, postal):
        if first:
            field = self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))
            field.clear()
            field.send_keys(first)
        if last:
            field = self.wait.until(EC.visibility_of_element_located(self.LAST_NAME))
            field.clear()
            field.send_keys(last)
        if postal:
            field = self.wait.until(EC.visibility_of_element_located(self.POSTAL_CODE))
            field.clear()
            field.send_keys(postal)
            
        self._js_click(self.CONTINUE_BTN)

    def finish_checkout(self):
        self._js_click(self.FINISH_BTN)
        self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER))

    def get_confirmation_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER)).text

    def get_error_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_BANNER)).text