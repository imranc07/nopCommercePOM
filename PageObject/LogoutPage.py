"""
LogoutPage.py contains all the methods related to the NopCommerce application Logout.

Page Object File
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

# Import the locator and LoginPage
from TestLocators.locators import NopCommerceLocators
from PageObject.LoginPage import NopCommerceLoginPage

# NopCommerceLogoutPage Class to handle user logout automation for NopCommerce.
class NopCommerceLogoutPage(NopCommerceLoginPage):
   
    def __init__(self):
        # Initialize the Chrome WebDriver and WebDriverWait
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
            
    def logout(self):
        try:
            # Ensure the user is logged in before attempting to logout
            if not self.user_login():
                print("Cannot logout because login failed.")
                return False

            # Perform logout
            logout_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, NopCommerceLocators.logout_button)))
            logout_button.click()

            # Validate successful logout by checking for the login menu presence
            login_menu = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, NopCommerceLocators.login_menu)))

            if login_menu.is_displayed():
                print("Logout successful!")
                return True
            else:
                print("Logout failed!")
                return False

        except (NoSuchElementException, TimeoutException, ElementNotVisibleException) as error:
            # Handle exceptions
            print(f"ERROR during logout: {error}")
            return False

        finally:
            # Close the browser
            self.driver.quit()

    # Method to fetch the current URL of the page
    def get_current_url(self):
        return self.driver.current_url
