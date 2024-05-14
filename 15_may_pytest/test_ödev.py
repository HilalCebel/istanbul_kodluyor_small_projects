from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest

import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# test fonksiyonları buraya gelecek


# def setup_method(self):
#         #her test başlangıcında çalışacak fonksiyon
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window() 
#         self.driver.get("https://www.saucedemo.com/")

# def teardown_method(self):
#         #her test bitiminde çalışacak fonksiyon
#         self.driver.quit()

pytest
def test_empty_username(browser):
    browser.get("https://www.saucedemo.com/")
    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()
    error = browser.find_element(By.XPATH, "//h3[@data-test='error']")
    error_message = error.text
    assert error_message == "Epic sadface: Username is required"
    sleep(5)

def test_empty_password(browser):
    browser.get("https://www.saucedemo.com/")
    user_name = browser.find_element(By.ID, "user-name")
    user_name.send_keys("standard_user")
    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()
    error = browser.find_element(By.XPATH, "//h3[@data-test='error']")
    error_message = error.text
    assert error_message == "Epic sadface: Password is required"
    sleep(5)

def test_locked_user(browser):
    browser.get("https://www.saucedemo.com/")
    user_name = browser.find_element(By.ID, "user-name")
    user_name.send_keys("locked_out_user")
    password_name = browser.find_element(By.ID, "password")
    password_name.send_keys("secret_sauce")
    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()
    error = browser.find_element(By.XPATH, "//h3[@data-test='error']")
    error_message = error.text
    assert error_message == "Epic sadface: Sorry, this user has been locked out."
    sleep(5)

def test_successful_login_and_product_count(browser):
    browser.get("https://www.saucedemo.com/")
    user_name = browser.find_element(By.ID, "user-name")
    user_name.send_keys("standard_user")
    password_name = browser.find_element(By.ID, "password")
    password_name.send_keys("secret_sauce")
    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()
    products = browser.find_elements(By.CLASS_NAME, "inventory_item_description")
    assert len(products) == 6
    sleep(5)

def test_add_to_cart(browser):
    browser.get("https://www.saucedemo.com/")
    user_name = browser.find_element(By.ID, "user-name")
    user_name.send_keys("standard_user")
    password_name = browser.find_element(By.ID, "password")
    password_name.send_keys("secret_sauce")
    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()
    add_cart = browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_cart.click()
    sleep(5)
