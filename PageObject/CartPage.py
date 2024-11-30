"""
CartPage.py contains all the methods related to the Cart Page.

Page Object File.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Import exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException

# Import the webdriver wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import data and locators
from TestData.data import NopCommerceData
from TestLocators.locators import NopCommerceLocators

# NopCommerceCartPage Class to handle shopping cart interactions on the NopCommerce website.
class NopCommerceCartPage:

    # Initializes the WebDriver and sets up an explicit wait.
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 30)

    # start() method to launch the browser, maximizes the window, and navigates to the home page.
    def start(self):
        self.driver.maximize_window()
        self.driver.get(NopCommerceData.url)

    # add_to_cart() method to automate the process of adding a product to the cart.
    def add_to_cart(self):
        try:
            # Select a product
            select_product = self.wait.until(EC.visibility_of_element_located((By.XPATH, NopCommerceLocators.select_any_product)))
            select_product.click()

            # Click the "Add to Cart" button
            add_cart = self.wait.until(EC.element_to_be_clickable((By.XPATH, NopCommerceLocators.add_cart)))
            add_cart.click()

            # Verify success message
            add_to_cart_success_message_text = self.wait.until(EC.visibility_of_element_located((By.XPATH, NopCommerceLocators.add_card_success_message))).text
            if add_to_cart_success_message_text == "The product has been added to your ":
                print("Product successfully added to cart!")
                return True
            else:
                print("Shopping Cart is empty!")
                return False

        except (NoSuchElementException, TimeoutException, ElementNotVisibleException) as error:
            # Handle exceptions
            print(f"Error adding product to cart: {error}")
            return False

    # shopping_cart() method to automate the process of navigating to the shopping cart and verifying its contents.
    def shopping_cart(self):
        try:
            # Click on the shopping cart menu
            shopping_cart = self.wait.until(EC.element_to_be_clickable((By.XPATH, NopCommerceLocators.shopping_cart_menu)))
            shopping_cart.click()

            # Verify the cart total
            cart_total_text = self.wait.until(EC.presence_of_element_located((By.XPATH, NopCommerceLocators.cart_total))).text
            if cart_total_text == "$245.00":
                print("Cart details are verified!")
                return True
            else:
                print("Cart details mismatch!")
                return False

        except (NoSuchElementException, TimeoutException, ElementNotVisibleException) as error:
            # Handle exceptions
            print(f"Error verifying cart details: {error}")
            return False

    # remove_cart_product() method to automate the process of removing a product from the cart
    def remove_cart_product(self):
        try:
            # Click on the "Remove" button for a product
            remove_product = self.wait.until(EC.element_to_be_clickable((By.XPATH, NopCommerceLocators.remove_button)))
            remove_product.click()

            # Verify the cart is empty
            shopping_cart_text = self.wait.until(EC.presence_of_element_located((By.XPATH, NopCommerceLocators.empty_cart_text))).text
            if shopping_cart_text == "Your Shopping Cart is empty!":
                print("Product successfully removed from cart!")
                return True
            else:
                print("Something went wrong!")
                return False

        except (NoSuchElementException, TimeoutException, ElementNotVisibleException) as error:
            # Handle exceptions
            print(f"Error removing product from cart: {error}")
            return False

        finally:
            # Close the browser after completing the operation
            self.driver.quit()
