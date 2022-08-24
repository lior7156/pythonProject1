from selenium import webdriver
from selenium.webdriver.common.by import By
# wd
class Aos_Cart:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def total_quantity(self):
        """method that returns the total quantity of product in cart window"""
        return self.driver.find_element(By.CSS_SELECTOR, "span>label.roboto-regular")

    def cart_window_productcolor(self):
        """method that returns the colors of the products in the cart"""
        list_colors = []
        list_colors1 = self.driver.find_elements(By.CSS_SELECTOR, 'label>span.ng-binding')
        for i in list_colors1:
            list_colors.append(i.text)
        return list_colors[::-1]

    def card_windows_productprice(self):
        """method that returns the prices of the products in the cart"""
        list_price = []
        price = self.driver.find_elements(By.CSS_SELECTOR, 'p.price')
        for i in price:
            list_price.append(float(i.text.replace(",", "").replace("$", "")))
        return list_price[::-1]

    def cart_window_productname(self):
        """method that returns the names of the products in the cart"""
        list_1 = []
        list_name = self.driver.find_elements(By.CSS_SELECTOR, "table>tbody>tr>td>a>h3")
        for i in list_name:
            list_1.append(i.text)
        return list_1[::-1]

    def cart_window_product_quantity(self):
        """method that returns the quantities of the products in the cart"""
        quantity = self.driver.find_elements(By.CSS_SELECTOR, "td>a>label.ng-binding")
        list_quantity = []
        for i in range(0, len(quantity)-1, 2):
            list_quantity.append(int(quantity[i].text.replace('QTY: ','')))
        return list_quantity[::-1]

    def product_name(self):
        """method that returns the name of product we choose"""
        name = self.driver.find_element(By.CSS_SELECTOR, "h1[class='roboto-regular screen768 ng-binding']")
        return name.text

    def product_price(self):
        """method that returns the price of product we choose"""
        price = self.driver.find_elements(By.CSS_SELECTOR, "h2[class='roboto-thin screen768 ng-binding']")
        return float(price[0].text.replace(",", "").replace("$", ""))

    def product_colors(self):
        """method that returns the colors of product we choose"""
        color = self.driver.find_element(By.CSS_SELECTOR, ".colorSelected")
        return color.get_attribute("title")

    def product_quantity(self):
        """method that returns the quantities of product we choose"""
        return int(self.driver.find_element(By.CSS_SELECTOR, '[name="quantity"]').get_attribute("value"))

    def cart_total_in_window(self):
        """method that returns a total price text in shopping cart window"""
        return self.driver.find_elements(By.CSS_SELECTOR, ".cart-total")[0].text

    def cart_total_table(self):
        """method that returns a total price text in shopping cart page"""
        return self.driver.find_elements(By.CSS_SELECTOR, "span.roboto-medium")[3].text

    def num_of_products(self):
        """method that show the number of the product in the cart"""
        products_number = self.driver.find_element(By.CSS_SELECTOR, "#shoppingCartLink>[class='cart ng-binding']")
        return products_number.text