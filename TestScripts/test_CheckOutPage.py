"""
test_CheckOutPage.py contains the test cases for the Checkout Page.

Test Scripts File.
"""

from PageObject.CheckOutPage import NopCommerceCheckOutPage

# Test case to validate the checkout process
def test_checkout():
    checkout_page = NopCommerceCheckOutPage()
    checkout_success = checkout_page.checkout()
    assert checkout_success == True
    print("Checkout process completed successfully.")

    # Verify that the user receives an order confirmation with a unique order number
    order_number_id = checkout_page.get_order_number()
    assert order_number_id
    print(f"Order confirmation received with Order Number: {order_number_id}")
