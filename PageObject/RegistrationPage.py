"""
RegistrationPage.py contains all the methods related to NopCommerce Registration Page.

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

# Import the data and locator
from TestData.data import NopCommerceData
from TestLocators.locators import NopCommerceLocators

# NopCommerceRegistration class to handle user registration automation for NopCommerce
class NopCommerceRegistration:
    def __init__(self):
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            self.wait = WebDriverWait(self.driver, 20)

    # start() method to launch the browser, maximize the window, and navigate to the home page.
    def start(self):
            self.driver.maximize_window()
            self.driver.get(NopCommerceData.url)

    # register_user() method to automates the user registration process, including filling in the date of birth, and validates successful registration.
    def register_user(self):        
        try:
            registration_menu = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, NopCommerceLocators.registration_menu)))
            registration_menu.click()

            # Click Gender Button
            gender_button = self.wait.until(EC.element_to_be_clickable((By.ID, NopCommerceLocators.gender_button)))
            gender_button.click()
 
            # Enter First Name
            self.wait.until(EC.presence_of_element_located((By.ID, NopCommerceLocators.firstname_locator))).send_keys(NopCommerceData.firstname)

            # Enter Last Name
            self.wait.until(EC.presence_of_element_located((By.ID, NopCommerceLocators.lastname_locator))).send_keys(NopCommerceData.lastname)

            # Fill Date of Birth
            day_dropdown = self.wait.until(EC.presence_of_element_located((By.XPATH, NopCommerceLocators.dob_day)))
            month_dropdown = self.wait.until(EC.presence_of_element_located((By.XPATH, NopCommerceLocators.dob_month)))
            year_dropdown = self.wait.until(EC.presence_of_element_located((By.XPATH, NopCommerceLocators.dob_year)))
            Select(day_dropdown).select_by_value("15")
            Select(month_dropdown).select_by_value("5")
            Select(year_dropdown).select_by_value("2000")
 
            # Enter Email
            self.wait.until(EC.presence_of_element_located((By.ID, NopCommerceLocators.email_locator))).send_keys(NopCommerceData.email)

            # Enter Password and Confirm
            self.wait.until(EC.presence_of_element_located((By.ID, NopCommerceLocators.password_locator))).send_keys(NopCommerceData.password)
            self.wait.until(EC.presence_of_element_located((By.ID, NopCommerceLocators.confirm_password_locator))).send_keys(NopCommerceData.password)

            # Click Register Button
            self.wait.until(EC.element_to_be_clickable((By.ID, NopCommerceLocators.register_button))).click()

            # Validate Success Message
            success_message_text = self.wait.until(EC.presence_of_element_located((By.XPATH, NopCommerceLocators.success_message))).text

            if success_message_text == "Your registration completed":
                print("Registration successful!")
                return True
            else:
                print("Registration failed. Unexpected error!")
                return False

        except (NoSuchElementException, TimeoutException, ElementNotVisibleException) as error:
            # Handle exceptions
            print(f"ERROR during registration: {error}")
            return False

        finally:
            # Close the browser
            self.driver.quit()
