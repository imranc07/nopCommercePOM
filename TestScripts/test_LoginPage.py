"""
test_LoginPage.py contains the test cases for the Login Page.

Test Scripts File
"""

from PageObject.LoginPage import NopCommerceLoginPage

# Test case for validating valid user login functionality.
def test_user_login():
    login_page = NopCommerceLoginPage()
    login_page.start()
    assert login_page.user_login() == True
    print("Login successful!")

# Test case for validating user login functionality with invalid email.
def test_invalid_email_login():
    login_page = NopCommerceLoginPage()
    login_page.start()
    assert login_page.invalid_email_login() == True
    print("Success: Login Failed due to invalid email!")

# Test case for validating user login functionality with invalid password.
def test_invalid_password_login():
    """
    Test case for validating user login functionality.
    """
    login_page = NopCommerceLoginPage()
    login_page.start()
    assert login_page.invalid_password_login() == True
    print("Success: Login Failed due to invalid password!")


