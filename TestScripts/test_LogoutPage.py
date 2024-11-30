"""
test_LogoutPage.py contains the test cases for the Logout Page.

Test Scripts File
"""

from PageObject.LogoutPage import NopCommerceLogoutPage

# Test case for validating the logout functionality for a valid user.
def test_logout():
    logout_page = NopCommerceLogoutPage()
    logout_page.start()
    assert logout_page.logout() == True, "Logout action failed"
    print("Logout successful!")
    
    # Verify the user is redirected to the expected page after logout
    redirected_url = logout_page.get_current_url()
    expected_url = "https://demo.nopcommerce.com/"
    
    # Assert the current URL matches the expected redirection URL
    assert redirected_url == expected_url, f"Redirection failed! Expected {expected_url}, but got {redirected_url}"
    print("Redirection to homepage/login page verified successfully!")
