"""
test_RegistrationPage.py contains the test cases for Registration Page.

Test Scripts File
"""

from PageObject.RegistrationPage import NopCommerceRegistration

# test case for new user registration
def test_register_user():
    registration_page = NopCommerceRegistration()
    registration_page.start()
    assert registration_page.register_user() == True
    print("Success: Your registration completed!")
