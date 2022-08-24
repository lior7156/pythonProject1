from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from project_AOS.Aos_Product import Aos_Product
# as
class Login_Payment:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.aos_product = Aos_Product(self.driver)

    def registration(self, email: str, name: str, password: str):
        """method that register to the site"""
        self.click_cart_icon()
        self.click_checkout()
        while True:
            try:
                self.driver.find_element(By.ID, "registration_btnundefined").click()
                break
            except:
                pass
        username = self.driver.find_element(By.CSS_SELECTOR, "[name='usernameRegisterPage']")
        username.send_keys(name)
        email1 = self.driver.find_element(By.CSS_SELECTOR, "[name='emailRegisterPage']")
        email1.send_keys(email)
        password1 = self.driver.find_element(By.CSS_SELECTOR, "[name='passwordRegisterPage']")
        password1.send_keys(password)
        password_confirm = self.driver.find_element(By.CSS_SELECTOR, "[name='confirm_passwordRegisterPage']")
        password_confirm.send_keys(password)
        agree_ratio = self.driver.find_element(By.CSS_SELECTOR, "[name='i_agree']")
        agree_ratio.click()
        register = self.driver.find_element(By.ID, "register_btnundefined")
        register.click()

    def shopping_cart_page(self):
        """to enter shopping cart page"""
        self.driver.find_element(By.ID, "menuCart").click()

    def click_user_icon(self):
        """click on user icon"""
        self.driver.find_element(By.ID, "menuUser").click()

    def user_icon(self):
        """see user icon"""
        self.driver.find_element(By.ID, "menuUser")

    def login(self, name: str, password: str):
        """login to the site"""
        self.click_user_icon()
        username = self.driver.find_element(By.CSS_SELECTOR, "[name='username']")
        username.send_keys(name)
        password1 = self.driver.find_element(By.CSS_SELECTOR, "[name='password']")
        password1.send_keys(password)
        self.driver.find_element(By.ID, "sign_in_btnundefined").click()

    def click_login_checkout(self, name: str, Password: str):
        """method does login in checkout"""
        username1 = self.driver.find_element(By.CSS_SELECTOR, '[name="usernameInOrderPayment"]')
        username1.send_keys(name)
        Password1 = self.driver.find_element(By.CSS_SELECTOR, '[name="passwordInOrderPayment"]')
        Password1.send_keys(Password)
        self.driver.find_element(By.ID, 'login_btnundefined').click()

    def logout(self):
        """logout from the site"""
        while True:
            try:
                user_icon = self.driver.find_element(By.CSS_SELECTOR, "[id='hrefUserIcon'][title='USER']")
                user_icon.click()
                break
            except:
                pass
        logout = self.driver.find_element(By.CSS_SELECTOR, "[translate='Sign_out'][ng-click='signOut($event)']")
        logout.click()

    def payment(self, safepay_username: str, safepay_password: str):
        """method that set payment for user"""
        self.click_cart_icon()
        self.click_checkout()
        while True:
            try:
                self.driver.find_element(By.ID, "next_btn").click()
                break
            except:
                pass
        self.driver.find_element(By.CSS_SELECTOR, "[name='safepay']").click()
        username = self.driver.find_element(By.CSS_SELECTOR, "[name='safepay_username']")
        username.send_keys(safepay_username)
        password = self.driver.find_element(By.CSS_SELECTOR, "[name='safepay_password']")
        password.send_keys(safepay_password)
        self.driver.find_element(By.ID, "pay_now_btn_SAFEPAY").click()

    def order_payment_login(self, username: str, password: str):
        """log in when you registered"""
        username1 = self.driver.find_element(By.CSS_SELECTOR, "[name='usernameInOrderPayment']")
        username1.send_keys(username)
        password1 = self.driver.find_element(By.CSS_SELECTOR, "[name='passwordInOrderPayment']")
        password1.send_keys(password)
        login = self.driver.find_element(By.ID, "login_btnundefined")
        login.click()
        next_button = self.driver.find_element(By.ID, "next_btn")
        next_button.click()

    def mastercard(self):
        """choose mastercard option"""
        master_cart_btn = self.driver.find_element(By.CSS_SELECTOR, '[alt="Master credit"]')
        master_cart_btn.click()

    def card_number(self, card_number: int):
        """enter card number"""
        card_number1 = self.driver.find_element(By.ID, "creditCard")
        card_number1.send_keys(card_number)

    def cvv(self, cvv: int):
        """enter cvv number"""
        cvv1 = self.driver.find_element(By.CSS_SELECTOR, "[name='cvv_number']")
        cvv1.send_keys(cvv)

    def card_holder_name(self, name: str):
        """enter cardholder name"""
        cardholder = self.driver.find_element(By.CSS_SELECTOR, "[name='cardholder_name']")
        cardholder.send_keys(name)

    def card_date(self, month, year):
        """choose Card validity"""
        month1 = self.driver.find_element(By.CSS_SELECTOR, '[name="mmListbox"]')
        select_month = Select(month1)
        select_month.select_by_value(month)
        year1 = self.driver.find_element(By.CSS_SELECTOR, '[name="yyyyListbox"]')
        select_year = Select(year1)
        select_year.select_by_value(year)

    def unsave_changes_btn(self):
        """method that click on button radio to unsave the credit card details"""
        self.driver.find_element(By.CSS_SELECTOR, "[name='save_master_credit']").click()

    def num_of_items_in_shopping_cart(self):
        """items number in the shopping cart"""
        num_of_items = self.driver.find_element(By.CSS_SELECTOR, '[id="mobileShoppingCart"]>tool-tip-cart>div>div>label>span')
        return num_of_items.text

    def my_orders_page(self):
        """go to my orders page"""
        self.click_user_icon()
        self.driver.find_element(By.CSS_SELECTOR, '[translate="My_Orders"][href="javascript:void(0)"]').click()

    def pay_now_mastercard(self):
        """click on pay now to pay"""
        while True:
            try:
                pay_now = self.driver.find_element(By.CSS_SELECTOR, "#pay_now_btn_ManualPayment[data-ng-click='senderCtrl.send()']")
                pay_now.click()
                break
            except:
                pass

    def click_checkout(self):
        """method that clicking on checkout"""
        self.click_cart_icon()
        self.driver.find_element(By.ID, "checkOutPopUp").click()

    def username_text(self):
        """method that show the username text"""
        username = self.driver.find_element(By.CSS_SELECTOR, '[class="hi-user containMiniTitle ng-binding"]')
        if username.text == "":
            raise Exception("there is no element of username when you logged out!!")
        return username.text

    def cart_icon(self):
        """see the cart icon"""
        self.driver.find_element(By.ID, "menuCart")

    def click_cart_icon(self):
        """click on cart icon"""
        self.driver.find_element(By.ID, "menuCart").click()

    def remove_product(self):
        """method that delete a product from the cart"""
        while True:
            try:
                remove = self.driver.find_element(By.CSS_SELECTOR, "[class='remove red ng-scope'][translate='REMOVE']")
                remove.click()
                break
            except:
                pass

    def edit(self):
        """method that edits the product we choose"""
        self.click_cart_icon()
        while True:
            try:
                list_edit = self.driver.find_elements(By.CSS_SELECTOR, "[class='edit ng-scope']")
                list_edit[0].click()
                break
            except:
                pass
        self.aos_product.Quantity_button_plus()
        self.aos_product.Quantity_button_plus()
        self.aos_product.Quantity_button_plus()
        self.aos_product.add_to_cart()

    def edit1(self):
        """method that edits the product we choose"""
        self.click_cart_icon()
        while True:
            try:
                list_edit = self.driver.find_elements(By.CSS_SELECTOR, "[class='edit ng-scope']")
                list_edit[1].click()
                break
            except:
                pass
        self.aos_product.Quantity_button_plus()
        self.aos_product.Quantity_button_plus()
        self.aos_product.Quantity_button_plus()
        self.aos_product.add_to_cart()

    def thank_you(self):
        """method that show a thank you text after the shopping"""
        while True:
            try:
                thank_you_text = self.driver.find_element(By.CSS_SELECTOR, "span[class='roboto-regular ng-scope']")
                return thank_you_text.text
            except:
                pass