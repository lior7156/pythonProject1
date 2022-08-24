from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#as
class Aos_Product:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def Quantity_button(self):
        quantity = self.driver.find_element(By.CSS_SELECTOR, "[name='quantity']")
        return quantity.text

    def Quantity_button_plus(self):
        """method that add number of quantity we want"""
        self.driver.find_element(By.CSS_SELECTOR, "[class='plus']").click()
        self.Quantity_button()

    def Quantity_button_minus(self):
        """method that add number of quantity we want"""
        self.driver.find_element(By.CSS_SELECTOR, "[class='minus']").click()
        self.Quantity_button()

    def Quantity_button_number(self, num: int):
        """method that ask for number to put for the Quantity"""
        quantity = self.Quantity_button()
        quantity.send_keys(Keys.CONTROL, "a")
        quantity.send_keys(num)

    def add_to_cart(self):
        """method that click on add to cart button"""
        self.driver.find_element(By.CSS_SELECTOR, "[name='save_to_cart']").click()

    def back_to_home(self):
        """method that click on site icon to back to home page"""
        self.driver.find_element(By.CSS_SELECTOR, "[ng-click='go_up()']").click()

    def navigate_to_home(self):
        """method that navigate to home page from navigate line"""
        self.driver.find_element(By.CSS_SELECTOR, "[translate='HOME']").click()

    def shopping_cart_toolbar(self):
        """method that returns shopping cart text on navigate line"""
        shopping_cart = self.driver.find_element(By.CSS_SELECTOR, "[class='select  ng-binding']")
        return shopping_cart.text