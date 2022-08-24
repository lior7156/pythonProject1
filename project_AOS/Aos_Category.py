from selenium import webdriver
from selenium.webdriver.common.by import By

class Aos_Category:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def back_to_home(self):
        """method that click on site icon to back to home page"""
        return self.driver.find_element(By.CSS_SELECTOR, "[ng-click='go_up()']").click()

    def product_by_id(self, num: str):
        """method that get ID of product"""
        return self.driver.find_element(By.ID, num)

    def click_product_by_id(self, num: str):
        """method that get id of product and clicking"""
        self.product_by_id(num).click()

    def navigate_to_home(self):
        """method that navigate to home page from navigate line"""
        return self.driver.find_element(By.CSS_SELECTOR, "[translate='HOME']").click()

    def navigate_to_tablets(self):
        """method that navigate to tablets if the tablets on toolbar"""
        self.driver.find_element(By.CSS_SELECTOR, "[class='ng-binding'][href='']").click()

    def tablets_toolbar(self):
        """method that show tablets text on toolbar"""
        tablets_toolbar = self.driver.find_element(By.CSS_SELECTOR, "[class='select  ng-binding']")
        return tablets_toolbar.text
