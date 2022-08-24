# from selenium import webdriver
# from selenium.webdriver.common.by import By
#ds
# class product_page:
#     def __init__(self, driver:webdriver):
#         self.driver = driver
#
#     def num_of_products(self):
#         """method that show the number of the product in the cart"""
#         products_number = self.driver.find_element(By.CSS_SELECTOR, "#shoppingCartLink>[class='cart ng-binding']")
#         return products_number.text
#
#     def product_price(self):
#         """returns product price"""
#         return self.driver.find_element(By.CSS_SELECTOR, '[class="roboto-thin ng-binding"]').text
#
#     def product_name(self):
#         """returns product name"""
#         return self.driver.find_element(By.CSS_SELECTOR, 'h1[class="roboto-regular ng-binding"]').text
#
#     def product_color(self):
#         """returns product color"""
#         color = self.driver.find_element(By.CSS_SELECTOR, ".colorSelected")
#         return color.get_attribute("title")
#
#     def product_quantity(self):
#         """returns product quantity"""
#         return self.driver.find_element(By.CSS_SELECTOR, '[name="quantity"]').text
#
#     def cart_product_price(self):
#         """shows the product price that in the right cart"""
#         return self.driver.find_element(By.CSS_SELECTOR, '[class="price roboto-regular ng-binding"]').text
#
#     def cart_product_name(self):
#         """shows the product name that in the right cart"""
#         return self.driver.find_element(By.CSS_SELECTOR, 'h3[class="ng-binding"]').text
#
#     def cart_product_quantity(self):
#         """shows the product quantity that in the right cart"""
#         return self.driver.find_element(By.XPATH, '//tr[@id="product"]/td[2]/a/label[1]').text
#
#     def cart_product_color(self):
#         """shows the product color that in the right cart"""
#         color = self.driver.find_element(By.CSS_SELECTOR, 'label>span.ng-binding')
#         return color.get_attribute("title").replace("''", "")
#
#     def product_int_price(self):
#         """int to product price"""
#         product_price = (self.driver.find_element(By.CSS_SELECTOR, '[class="roboto-thin ng-binding"]').text[1:]).replace(",", "")
#         return float(product_price)
#
#     def remove_product(self):
#         """to remove product from the right cart"""
#         self.driver.find_element(By.CSS_SELECTOR, '[class="removeProduct iconCss iconX"]').click()