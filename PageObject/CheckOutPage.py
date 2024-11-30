"""
CheckOutPage.py contains all the methods and logic related to the checkout process.

Page Object File.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

# Import necessary exceptions from Selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException

# Import the webdriver wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import test data and locators, Login Page and Cart Page
from TestData.data import NopCommerceData
from TestLocators.locators import NopCommerceLocators
from PageObject.LoginPage import NopCommerceLoginPage
from PageObject.CartPage import NopCommerceCartPage

# NopCommerceCheckOutPag() class to handle the checkout process in NopCommerce. Inherits from LoginPage and CartPage.
class NopCommerceCheckOutPage(NopCommerceLoginPage, NopCommerceCartPage):

    def __init__(self):
        """Initialize the WebDriver and explicit wait."""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 30)

        # call the superclass initializer
        super().__init__()

    # checkout() method to perform the checkout process
    def checkout(self):

        # Variable to store the fetched order number
        order_number = None  

        try:
            # Ensure the user is logged in
            if not self.user_login():
                print("Login failed, cannot proceed to checkout.")
                return False

            # Add a product to the cart and verify success
            if not self.add_to_cart():
                print("Failed to add product to cart, cannot proceed to checkout.")
                return False

            # Agree to terms and conditions
            self.wait.until(EC.element_to_be_clickable((By.ID, NopCommerceLocators.terms_checkbox))).click()

            # Proceed to the checkout page
            self.wait.until(EC.element_to_be_clickable((By.ID, NopCommerceLocators.checkout_button))).click()

            # Select country from dropdown
            country_dropdown = self.wait.until(EC.presence_of_element_located((By.ID, NopCommerceLocators.country_locator)))
            Select(country_dropdown).select_by_value("133")

            # Enter city Name
            self.wait.until(EC.presence_of_element_located((By.ID, NopCommerceLocators.city_locator))).send_keys(NopCommerceData.city_name)

            # Enter address line 1
            self.wait.until(EC.presence_of_element_located((By.ID, NopCommerceLocators.address_line1))).send_keys(NopCommerceData.address_line)
 
            # Enter Postal code
            self.wait.until(EC.presence_of_element_located((By.ID, NopCommerceLocators.postal_code_locator))).send_keys(NopCommerceData.postal_code)

            #Enter Phone Number
            self.wait.until(EC.presence_of_element_located((By.ID, NopCommerceLocators.phone_number_locator))).send_keys(NopCommerceData.phone_number)

            # Click on continue button during checkout, shipping and payment process
            self.wait.until(EC.element_to_be_clickable((By.XPATH, NopCommerceLocators.checkout_continue_button))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, NopCommerceLocators.shipping_continue_button))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, NopCommerceLocators.payment_continue_button))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, NopCommerceLocators.payment_info_continue_button))).click()

            # Confirm the order
            self.wait.until(EC.element_to_be_clickable((By.XPATH, NopCommerceLocators.confirm_button))).click()

            # Validate the success message after order confirmation
            success_message = self.wait.until(EC.presence_of_element_located((By.XPATH, NopCommerceLocators.confirm_order_success_message))).text
            if success_message == "Your order has been successfully processed!":
                print("Order has been successfully processed!")

                # Fetch and print the order number
                order_number = self.get_order_number()
                print(f"Order Number: {order_number}")
                return True
            else:
                print("Unexpected error occurred during checkout.")
                return False

        except (NoSuchElementException, TimeoutException, ElementNotVisibleException) as error:
            # Handle exceptions
            print(f"Error during checkout: {error}")
            return False

        finally:

            # If an order number is fetched, print it to the console. 
            if order_number:
                print(f"Fetched Order Number: {order_number}")
            
            # Close the browser.
            self.driver.quit()

    # get_order_number() method to retrieve the order number from the confirmation page
    def get_order_number(self):
        order_number_element = self.wait.until(EC.presence_of_element_located((By.XPATH, NopCommerceLocators.order_ID_text)))
        return order_number_element.text