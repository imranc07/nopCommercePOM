"""
LoginPage.py contains all the methods related to NopCommerce application positive and negative Login.

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

# Import the data and locator
from TestData.data import NopCommerceData
from TestLocators.locators import NopCommerceLocators

# NopCommerceLoginPage Class to handle user login automation for NopCommerce.
class NopCommerceLoginPage:
   
    def __init__(self):
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            self.wait = WebDriverWait(self.driver, 20)
            
    # start() method to launch the browser, maximize the window, and navigate to the home page.
    def start(self):
            self.driver.maximize_window()
            self.driver.get(NopCommerceData.url)

    # user_login() method to automate the user login process and validates successful login.
    def user_login(self):
        try:
            # Click on the login menu
            login_menu = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, NopCommerceLocators.login_menu)))
            login_menu.click()
 
            # Enter email
            email_field = self.wait.until(EC.presence_of_element_located((By.ID, NopCommerceLocators.email_locator)))
            email_field.send_keys(NopCommerceData.email)

            # Enter password
            password_field = self.wait.until(EC.presence_of_element_located((By.ID, NopCommerceLocators.password_locator)))
            password_field.send_keys(NopCommerceData.password)
 
            # Click Remember Me checkbox
            remember_me_checkbox = self.wait.until(EC.element_to_be_clickable((By.ID, NopCommerceLocators.rememberme_checkbox)))
            remember_me_checkbox.click()
 
            # Click Login button
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, NopCommerceLocators.login_button)))
            login_button.click()
 
            # Validate successful login
            my_account_text = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, NopCommerceLocators.myaccount_locator))).text

            if my_account_text == "My account":
                print("Login successful!")
                return True
            else:
                print("Login failed!")
                return False

        except (NoSuchElementException, TimeoutException, ElementNotVisibleException) as error:
            # Handle exceptions
            print(f"ERROR during login: {error}")
            return False

        finally:
            # Close the browser
            self.driver.quit()

    # invalid_password_login() method to automate the login process with an invalid password and validates the error message.
    def invalid_password_login(self):
        try:
            # Click on the login menu
            login_menu = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, NopCommerceLocators.login_menu)))
            login_menu.click()
 
            # Enter valid email
            email_field = self.wait.until(EC.presence_of_element_located((By.ID, NopCommerceLocators.email_locator)))
            email_field.send_keys(NopCommerceData.email)

            # Enter invalid password
            password_field = self.wait.until(EC.presence_of_element_located((By.ID, NopCommerceLocators.password_locator)))
            password_field.send_keys(NopCommerceData.invalid_password)

            # Click Remember Me checkbox
            remember_me_checkbox = self.wait.until(EC.element_to_be_clickable((By.ID, NopCommerceLocators.rememberme_checkbox)))
            remember_me_checkbox.click()

            # Click Login button
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, NopCommerceLocators.login_button)))
            login_button.click()

            # Validate error message
            login_error_message = self.wait.until(EC.presence_of_element_located((By.XPATH, NopCommerceLocators.login_error_message))).text

            if "Login was unsuccessful" in login_error_message:
                print("Error message displayed for invalid password as expected.")
                return True
            else:
                print("Unexpected behavior: No error message displayed.")
                return False

        except (NoSuchElementException, TimeoutException, ElementNotVisibleException) as error:
            # Handle exceptions
            print(f"ERROR during invalid password login: {error}")
            return False

        finally:
            # Close the browser
            self.driver.quit()

    # invalid_email_login() method to automate the login process with an invalid email and validates the error message.
    def invalid_email_login(self):
        try:
            # Click on the login menu
            login_menu = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, NopCommerceLocators.login_menu)))
            login_menu.click()

            # Enter invalid email
            email_field = self.wait.until(EC.presence_of_element_located((By.ID, NopCommerceLocators.email_locator)))
            email_field.send_keys(NopCommerceData.invalid_email)

            # Enter password
            password_field = self.wait.until(EC.presence_of_element_located((By.ID, NopCommerceLocators.password_locator)))
            password_field.send_keys(NopCommerceData.password)

            # Validate error message
            invalid_email_message = self.wait.until(EC.presence_of_element_located((By.XPATH, NopCommerceLocators.wrong_email_message))).text

            if "Wrong email" in invalid_email_message:
                print("Error message displayed for invalid email as expected.")
                return True
            else:
                print("Unexpected behavior: No error message displayed.")
                return False

        except (NoSuchElementException, TimeoutException, ElementNotVisibleException) as error:
            # Handle exceptions
            print(f"ERROR during invalid email login: {error}")
            return False

        finally:
            # Close the browser
            self.driver.quit()