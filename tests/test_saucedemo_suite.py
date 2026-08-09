import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_tc_func_01_valid_login(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    assert inventory.get_title_text() == "Products"

def test_tc_func_02_locked_out_user(driver):
    login = LoginPage(driver)
    login.load()
    login.login("locked_out_user", "secret_sauce")
    assert "Sorry, this user has been locked out." in login.get_error_message()

def test_tc_func_03_add_item_to_cart(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()
    assert inventory.get_cart_badge_count() == "1"

def test_tc_func_04_checkout_missing_postal(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()
    inventory.open_cart()
    checkout = CheckoutPage(driver)
    checkout.start_checkout()
    checkout.fill_customer_info("Jane", "Doe", "")
    assert "Postal Code is required" in checkout.get_error_text()

def test_tc_e2e_01_complete_checkout(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()
    inventory.open_cart()
    checkout = CheckoutPage(driver)
    checkout.start_checkout()
    checkout.fill_customer_info("Jane", "Doe", "K1P 1J1")
    checkout.finish_checkout()
    assert "thank you" in checkout.get_confirmation_text().lower()