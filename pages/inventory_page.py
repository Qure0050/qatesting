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
        return self.get_text(self.TITLE)

    def add_backpack_to_cart(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.ADD_BACKPACK))
        self.driver.execute_script("arguments[0].click();", btn)

    def get_cart_badge_count(self):
        return self.get_text(self.CART_BADGE)

    def open_cart(self):
        link = self.wait.until(EC.element_to_be_clickable(self.CART_LINK))
        self.driver.execute_script("arguments[0].click();", link)