from selenium import webdriver
from selenium.webdriver.common.by import By
# ds
class Aos_Home:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def category_speakers(self):
        """this method choose a specific category"""
        return self.driver.find_element(By.ID, "speakersImg")

    def click_category_speakers(self):
        """this method choose a specific category and click on him"""
        self.category_speakers().click()

    def category_tablets(self):
        """this method choose a specific category"""
        return self.driver.find_element(By.ID, "tabletsImg")

    def click_category_tablets(self):
        """this method choose a specific category and click on him"""
        self.category_tablets().click()

    def category_laptops(self):
        """this method choose a specific category"""
        return self.driver.find_element(By.ID, "laptopsImg")

    def click_category_laptops(self):
        """this method choose a specific category and click on him"""
        self.category_laptops().click()

    def category_headphones(self):
        """this method choose a specific category"""
        return self.driver.find_element(By.ID, "headphonesImg")

    def click_category_headphones(self):
        """this method choose a specific category and click on him"""
        self.category_headphones().click()

    def category_mice(self):
        """this method choose a specific category"""
        return self.driver.find_element(By.ID, "miceImg")

    def click_category_mice(self):
        """this method choose a specific category and click on him"""
        self.category_mice().click()

    def contact_us(self):
        """method the show the text contact us"""
        contact_us = self.driver.find_element(By.CSS_SELECTOR, "[class='roboto-bold contact_us ng-scope']")
        return contact_us.text