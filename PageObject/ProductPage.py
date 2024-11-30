"""
ProductPage.py contains all the methods related to the NopCommerce application Products.

Page Object File
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

# Import exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException

# Import the webdriver wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import the data and locators
from TestData.data import NopCommerceData
from TestLocators.locators import NopCommerceLocators

# NopCommerceProductPage Class to handle product-related automation for NopCommerce.
class NopCommerceProductPage:
   
    def __init__(self):
        # Initialize the Chrome WebDriver and WebDriverWait
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
            
    # start() method to launch the browser, maximize the window, and navigate to the home page.
    def start(self):
        self.driver.maximize_window()
        self.driver.get(NopCommerceData.url)

    # search_and_browse_product() method to automate product search, sort, and validation.
    def search_and_browse_product(self):
        try:
            # Enter search keyword in the search box
            search_box = self.wait.until(EC.presence_of_element_located((By.ID, NopCommerceLocators.search_box)))
            search_box.send_keys(NopCommerceData.search_keyword)
 
            # Click on the search button
            search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, NopCommerceLocators.search_button)))
            search_button.click()

            # Sort products by price (Low to High)
            sortby_dropdown = self.wait.until(EC.presence_of_element_located((By.ID, NopCommerceLocators.sortby_locator)))
            Select(sortby_dropdown).select_by_value("10")

            # Click on the searched product to view its details
            product = self.wait.until(EC.element_to_be_clickable((By.XPATH, NopCommerceLocators.product_locator)))
            product.click()

            # Validate the product details
            product_text = self.wait.until(EC.presence_of_element_located((By.XPATH, NopCommerceLocators.product_text))).text

            if product_text == "Samsung Galaxy S24 256GB":
                print("Product details successfully verified!")
                return True
            else:
                print("Product details do not match!")
                return False

        except (NoSuchElementException, TimeoutException, ElementNotVisibleException) as error:
            # Handle exceptions
            print(f"Error during product search and browse: {error}")
            return False

        finally:
            # Close the browser
            self.driver.quit()
