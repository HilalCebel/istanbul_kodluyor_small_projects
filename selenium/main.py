from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


#-Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.

def login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    error = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    error_message = error.text
    assert error_message == "Epic sadface: Username is required"
    sleep(5)
    

login()



#-Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.

def login2():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    user_name = driver.find_element(By.ID, "user-name")
    user_name.send_keys("standard_user")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    error = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    error_message = error.text
    assert error_message == "Epic sadface: Password is required"
    sleep(5)


login2()



#-Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.

def login3():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    user_name = driver.find_element(By.ID, "user-name")
    user_name.send_keys("locked_out_user")
    password_name = driver.find_element(By.ID, "password")
    password_name.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    error = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    error_message = error.text
    assert error_message == "Epic sadface: Sorry, this user has been locked out."
    sleep(5)

login3()


#-Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.

def login4():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    user_name = driver.find_element(By.ID, "user-name")
    user_name.send_keys("standard_user")
    password_name = driver.find_element(By.ID, "password")
    password_name.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    products = driver.find_elements(By.CLASS_NAME, "inventory_item_description")
    assert len(products) == 6
    sleep(5)

login4()



#-Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. Giriş yapıldıktan sonra kullanıcıya gösterilen ilk ürünü sepete ekleyebilmelidir.


def login5():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    user_name = driver.find_element(By.ID, "user-name")
    user_name.send_keys("standard_user")
    password_name = driver.find_element(By.ID, "password")
    password_name.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    products = driver.find_elements(By.CLASS_NAME, "inventory_item_description")
    add_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_cart.click()
    sleep(5)


login5()
    









