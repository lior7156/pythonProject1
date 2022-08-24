from unittest import TestCase
from project_AOS.AOS_Home import Aos_Home
from project_AOS.Aos_Product import Aos_Product
from project_AOS.Aos_Category import Aos_Category
from project_AOS.Aos_login_payment import Login_Payment
from project_AOS.Aos_Cart import Aos_Cart
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

class TestAos(TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\selenium1\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service_chrome)

        # get url and open the site
        self.driver.get("http://www.advantageonlineshopping.com/")
        self.driver.maximize_window()

        # in case an element is not found on the page, will try again for 10 seconds
        # before we get an error message
        self.driver.implicitly_wait(20)
        self.aos_home = Aos_Home(self.driver)
        self.aos_category = Aos_Category(self.driver)
        self.aos_product = Aos_Product(self.driver)
        self.aos_login_payment = Login_Payment(self.driver)
        self.aos_cart = Aos_Cart(self.driver)

    def test_number1(self):
        """count = the number of products"""
        count = 0
        """click on the category"""
        self.aos_home.click_category_speakers()
        """choose product where id is 20"""
        self.aos_category.click_product_by_id("20")
        """add 2 products to the cart"""
        self.aos_product.Quantity_button_plus()
        self.aos_product.add_to_cart()
        count += 2
        self.aos_category.back_to_home()
        """click on the category"""
        self.aos_home.click_category_tablets()
        """choose product where id is 16"""
        self.aos_category.click_product_by_id("16")
        """add 3 products to the cart"""
        self.aos_product.Quantity_button_plus()
        self.aos_product.Quantity_button_plus()
        self.aos_product.add_to_cart()
        count += 3
        self.aos_category.back_to_home()
        print(count)
        print(int(self.aos_cart.num_of_products()))
        """this test is checking that the cart will show the correct number of products"""
        self.assertEqual(int(self.aos_cart.num_of_products()), count)

    def test_number2(self):
        """choose 3 products"""
        list_color = []
        list_quantity = []
        list_name = []
        list_price = []
        self.aos_home.click_category_speakers()
        self.aos_category.click_product_by_id("25")
        self.aos_product.Quantity_button_plus()
        list_color.append(self.aos_cart.product_colors())
        list_quantity.append(self.aos_cart.product_quantity())
        list_price.append(self.aos_cart.product_price())
        list_name.append(self.aos_cart.product_name())
        self.aos_product.add_to_cart()
        self.aos_product.back_to_home()

        self.aos_home.click_category_headphones()
        self.aos_category.click_product_by_id("15")
        self.aos_product.Quantity_button_plus()
        self.aos_product.Quantity_button_plus()
        list_color.append(self.aos_cart.product_colors())
        list_quantity.append(self.aos_cart.product_quantity())
        list_price.append(self.aos_cart.product_price())
        list_name.append(self.aos_cart.product_name())
        self.aos_product.add_to_cart()
        self.aos_product.back_to_home()

        self.aos_home.click_category_tablets()
        self.aos_category.click_product_by_id("16")
        self.aos_product.Quantity_button_plus()
        list_color.append(self.aos_cart.product_colors())
        list_quantity.append(self.aos_cart.product_quantity())
        list_price.append(self.aos_cart.product_price())
        list_name.append(self.aos_cart.product_name())
        self.aos_product.add_to_cart()
        self.aos_product.back_to_home()

        print(list_quantity)
        print(list_price)
        print(list_color)
        print(list_name)

        """check if the quantities, colors, names, and prices are the same in cart window and products page"""
        for i in range(len(list_color)-1):
            self.assertEqual(list_color[i], self.aos_cart.cart_window_productcolor()[i])
            # self.assertEqual(list_name[i], self.aos_cart.cart_window_productname()[i])
            self.assertEqual(list_price[i]*list_quantity[i], self.aos_cart.card_windows_productprice()[i])
            self.assertEqual(list_quantity[i], self.aos_cart.cart_window_product_quantity()[i])

    def test_number3(self):
        """add 2 product to cart and remove one of them"""
        self.aos_home.click_category_speakers()
        self.aos_category.click_product_by_id("25")
        self.aos_product.add_to_cart()
        self.aos_category.back_to_home()

        self.aos_home.click_category_headphones()
        self.aos_category.click_product_by_id("15")
        self.aos_product.add_to_cart()
        self.aos_login_payment.click_cart_icon()
        self.aos_login_payment.remove_product()

        """check if after removing the number of products is 1"""
        print(len(self.aos_cart.num_of_products()))
        self.assertEqual(len(self.aos_cart.num_of_products()), 1)

    def test_number4(self):
        """choose a product and check if the product is in the cart"""
        self.aos_home.click_category_speakers()
        self.aos_category.click_product_by_id("25")
        self.aos_product.add_to_cart()
        self.aos_login_payment.click_cart_icon()

        """check if the text on toolbar is Shopping cart"""
        print(self.aos_product.shopping_cart_toolbar())
        self.assertEqual(self.aos_product.shopping_cart_toolbar(), "SHOPPING CART")

    def test_number5(self):
        """choose 3 products"""
        self.aos_home.click_category_speakers()
        self.aos_category.click_product_by_id("25")
        self.aos_product.Quantity_button_plus()
        self.aos_product.add_to_cart()
        self.aos_product.back_to_home()

        self.aos_home.click_category_speakers()
        self.aos_category.click_product_by_id("20")
        self.aos_product.add_to_cart()
        self.aos_product.back_to_home()

        self.aos_home.click_category_headphones()
        self.aos_category.click_product_by_id("15")
        self.aos_product.Quantity_button_plus()
        self.aos_product.add_to_cart()

        """click on cart icon to open the shopping cart"""
        self.aos_login_payment.click_cart_icon()
        list_quantity = self.aos_cart.cart_window_product_quantity()
        list_price = self.aos_cart.card_windows_productprice()
        list_name = self.aos_cart.cart_window_productname()
        print("=================")
        print(list_name)
        print("=================")
        print(list_price)
        print("=================")
        print(list_quantity)
        print("=================")
        print(self.aos_cart.cart_total_in_window())
        print("================")
        print(self.aos_cart.cart_total_table())
        """test that check if the total price is the same in cart table and cart window"""
        self.assertEqual(self.aos_cart.cart_total_in_window(), self.aos_cart.cart_total_table())

    def test_number6(self):
        """choose 2 products and edit him"""
        count = 0
        self.aos_home.click_category_tablets()
        self.aos_category.click_product_by_id("16")
        self.aos_product.add_to_cart()
        self.aos_product.back_to_home()
        count += 1
        self.aos_home.click_category_speakers()
        self.aos_category.click_product_by_id("20")
        self.aos_product.add_to_cart()
        self.aos_product.back_to_home()
        count += 1
        """edit first product"""
        self.aos_login_payment.edit()
        count += 3

        self.aos_product.back_to_home()
        """edit second product"""
        self.aos_login_payment.edit1()
        count += 3

        self.aos_product.back_to_home()
        print(count)
        """test that trying to check if the number of products is the same as the count"""
        self.assertEqual(self.aos_cart.num_of_products(), count)
        """the test was failed because the site can't edit the second product, only the first one"""

    def test_number7_1(self):
        """open tablets category"""
        self.aos_home.click_category_tablets()
        """choose product by id"""
        self.aos_category.click_product_by_id("16")
        """add to cart"""
        self.aos_product.add_to_cart()
        """return to tablets page"""
        self.aos_category.navigate_to_tablets()

        print(self.aos_category.tablets_toolbar())
        """test that check if the navigation to tablets page was succeeded"""
        self.assertEqual(self.aos_category.tablets_toolbar(), "TABLETS")

    def test_number7_2(self):
        """open tablets category"""
        self.aos_home.click_category_tablets()
        """choose product by id"""
        self.aos_category.click_product_by_id("16")
        """add to cart"""
        self.aos_product.add_to_cart()
        """return to tablets page"""
        self.aos_category.navigate_to_tablets()
        """return to home page"""
        self.aos_category.navigate_to_home()

        print(self.aos_home.contact_us())
        """test that check if the navigation to home page was succeeded"""
        self.assertEqual(self.aos_home.contact_us(), 'CONTACT US')

    def test_number8(self):
        """register to new account and try to pay for 2 products"""
        """click to tablets"""
        self.aos_home.click_category_tablets()
        """search product"""
        self.aos_category.click_product_by_id("16")
        """add to cart"""
        self.aos_product.add_to_cart()
        """back to home"""
        self.aos_product.back_to_home()

        self.aos_home.click_category_headphones()
        self.aos_category.click_product_by_id("15")
        self.aos_product.add_to_cart()
        self.aos_category.back_to_home()

        """register to account with email, username and password"""
        self.aos_login_payment.registration("lior1254@gmail.com", "Lior2624", "Lior2624")
        """set a payment details and trying to pay"""
        self.aos_login_payment.payment("Lior1195", "Lior1195")
        sleep(4)

        """ test that trying to compere between the text after the payment and the function(check if the payment was succeeded)"""
        self.assertEqual(self.aos_login_payment.thank_you(), "Thank you for buying with Advantage")
        """the test was failed because we can't click on pay now button when we register to the account: it's a bug"""

    def test_number9(self):
        """do order with exist user and mastercard"""
        self.aos_home.click_category_tablets()
        self.aos_category.click_product_by_id("16")
        self.aos_product.add_to_cart()
        self.aos_product.back_to_home()

        self.aos_home.click_category_headphones()
        self.aos_category.click_product_by_id("15")
        self.aos_product.add_to_cart()

        self.aos_login_payment.click_cart_icon()
        self.aos_login_payment.click_checkout()
        self.aos_login_payment.order_payment_login("Lior7152", "Lior7152")
        self.aos_login_payment.mastercard()
        self.aos_login_payment.card_number(444444444444)
        sleep(1)
        self.aos_login_payment.cvv(4444)
        self.aos_login_payment.card_holder_name("Lior")
        self.aos_login_payment.unsave_changes_btn()
        sleep(1)
        self.aos_login_payment.pay_now_mastercard()
        """test that trying to compere between the text after the payment and the function(check if the payment was succeeded)"""
        self.assertEqual(self.aos_login_payment.thank_you(), "Thank you for buying with Advantage")
        self.aos_login_payment.shopping_cart_page()
        """test that check if the number of items in the cart after the shopping is 0"""
        self.assertEqual('0', self.aos_login_payment.num_of_items_in_shopping_cart())
        """there is a bug and the test cant run because we cant click on pay button to complete the order!"""

    def test_number10_1(self):
        """log in to the site"""
        self.aos_login_payment.login("Lior8899", "Lior8899")
        """test that check if log in was succeeded"""
        self.assertTrue(self.aos_login_payment.username_text() == "Lior8899")
        print(self.aos_login_payment.username_text())

    def test_number10_2(self):
        """log in and log out from the site"""
        self.aos_login_payment.login("Lior8899", "Lior8899")
        self.aos_login_payment.logout()

        """test that trying to compere Lior8899 with no element"""
        with self.assertRaises(Exception):
            self.assertEqual(self.aos_login_payment.username_text(), "Lior8899")

    def tearDown(self):
        self.driver.close()