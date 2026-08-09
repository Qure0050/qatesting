import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def get_title_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.TITLE)).text

    def add_backpack_to_cart(self):
        btn = self.wait.until(EC.presence_of_element_located(self.ADD_BACKPACK))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        self.driver.execute_script("arguments[0].click();", btn)
        time.sleep(0.5)

    def get_cart_badge_count(self):
        return self.wait.until(EC.visibility_of_element_located(self.CART_BADGE)).text

    def open_cart(self):
        link = self.wait.until(EC.presence_of_element_located(self.CART_LINK))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", link)
        self.driver.execute_script("arguments[0].click();", link)
        time.sleep(1)