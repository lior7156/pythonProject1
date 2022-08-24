from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from project_AOS.AOS_Home import Aos_Home
from project_AOS.Aos_Product import Aos_Product
from project_AOS.Aos_Category import Aos_Category
from project_AOS.Aos_login_payment import Login_Payment
# sd

service_chrome = Service(r"C:\selenium1\chromedriver.exe")
driver = webdriver.Chrome(service=service_chrome)

aos_home = Aos_Home(driver)
aos_category = Aos_Category(driver)
aos_product = Aos_Product(driver)
aos_icon = Login_Payment(driver)

# get url and open the site
driver.get("http://www.advantageonlineshopping.com/")
driver.maximize_window()

# in case an element is not found on the page, will try again for 10 seconds
# before we get an error message
driver.implicitly_wait(10)

aos_icon.login("Lior8899", "Lior8899")
aos_icon.logout()
#1
# click on speakers to open this page
# Speakers = driver.find_element(By.ID, "speakersImg")
# Speakers.click()

# product_speakers = driver.find_element(By.ID, "20")
# product_speakers.click()
#
# Quantity = driver.find_element(By.CSS_SELECTOR, "[class='plus']")
# Quantity.click()
#
# Add_to_cart = driver.find_element(By.CSS_SELECTOR, "[name='save_to_cart']")
# Add_to_cart.click()
#
# back_to_home = driver.find_element(By.CSS_SELECTOR, "[ng-click='go_up()']")
# back_to_home.click()
#
# Tablets = driver.find_element(By.ID, "tabletsImg")
# Tablets.click()

# product_tablets = driver.find_element(By.ID, "16")
# product_tablets.click()
#
# Quantity = driver.find_element(By.CSS_SELECTOR, "[class='plus']")
# Quantity.click()
# Quantity.click()
#
# Add_to_cart = driver.find_element(By.CSS_SELECTOR, "[name='save_to_cart']")
# Add_to_cart.click()
#
# back_to_home = driver.find_element(By.CSS_SELECTOR, "[ng-click='go_up()']")
# back_to_home.click()

#2
# Laptops = driver.find_element(By.ID, "laptopsImg")
# Laptops.click()
#
# product_laptops = driver.find_element(By.CSS_SELECTOR, "[class='productName ng-binding']")
# product_laptops.click()
#
# Add_to_cart = driver.find_element(By.CSS_SELECTOR, "[name='save_to_cart']")
# Add_to_cart.click()
#
# back_to_home = driver.find_element(By.CSS_SELECTOR, "[ng-click='go_up()']")
# back_to_home.click()

#3
# cart_button = driver.find_element(By.ID, "menuCart")
# cart_button.click()
# while True:
#     try:
#         list_remove = driver.find_elements(By.CSS_SELECTOR, "[class='remove red ng-scope']")
#         list_remove[0].click()
#         break
#     except:
#         pass
#
# back_to_home = driver.find_element(By.CSS_SELECTOR, "[ng-click='go_up()']")
# back_to_home.click()

#6
# cart_button = driver.find_element(By.ID, "menuCart")
# cart_button.click()
# while True:
#     try:
#         list_edit = driver.find_elements(By.CSS_SELECTOR, "[class='edit ng-scope']")
#         list_edit[0].click()
#         break
#     except:
#         pass
#
# Quantity = driver.find_element(By.CSS_SELECTOR, "[class='minus']")
# Quantity.click()
#
# Add_to_cart = driver.find_element(By.CSS_SELECTOR, "[name='save_to_cart']")
# Add_to_cart.click()
#
# back_to_home = driver.find_element(By.CSS_SELECTOR, "[ng-click='go_up()']")
# back_to_home.click()

#7
# Tablets = driver.find_element(By.ID, "tabletsImg")
# Tablets.click()
#
# product_tablets = driver.find_element(By.ID, "16")
# product_tablets.click()
#
# navigate_line_tablets = driver.find_element(By.CSS_SELECTOR, "[class='ng-binding'][href='']")
# navigate_line_tablets.click()
#
# navigate_to_home = driver.find_element(By.CSS_SELECTOR, "[translate='HOME']")
# navigate_to_home.click()

#8

# checkout = driver.find_element(By.ID, "checkOutPopUp")
# checkout.click()

# registery = driver.find_element(By.ID, "registration_btnundefined").click()
# username = driver.find_element(By.CSS_SELECTOR, "[name='usernameRegisterPage']")
# username.send_keys("Lior8899")
# email = driver.find_element(By.CSS_SELECTOR, "[name='emailRegisterPage']")
# email.send_keys("lior7156@gmail.com")
# password = driver.find_element(By.CSS_SELECTOR, "[name='passwordRegisterPage']")
# password.send_keys("Lior8899")
# password_confirm = driver.find_element(By.CSS_SELECTOR, "[name='confirm_passwordRegisterPage']")
# password_confirm.send_keys("Lior8899")
# agree_ratio = driver.find_element(By.CSS_SELECTOR, "[name='i_agree']")
# agree_ratio.click()
# register = driver.find_element(By.CSS_SELECTOR, "[id='register_btnundefined']")
# register.click()





# username1 = driver.find_element(By.CSS_SELECTOR, "[class='ng-pristine ng-untouched ng-valid ng-scope'][name='usernameInOrderPayment']")
# username1.send_keys("Ohad8899")
# password1 = driver.find_element(By.CSS_SELECTOR, "[name='passwordInOrderPayment']")
# password1.send_keys("Ohad8899")
# login = driver.find_element(By.ID, "login_btnundefined")
# login.click()


# table = driver.find_element(By.CSS_SELECTOR, "[class='fixedTableEdgeCompatibility']")
# tr_list = table.find_elements(By.TAG_NAME, "tr")

