"""
test_CartPage.py contains the test cases for the Cart Page.

Test Scripts File.
"""

from PageObject.CartPage import NopCommerceCartPage

# Test case for validating the functionality of adding a product to the cart.
def test_add_to_cart():
    cart_page = NopCommerceCartPage()
    cart_page.start()
    assert cart_page.add_to_cart() == True
    print("Product successfully added to cart!")

# Test case for validating the shopping cart details.
def test_shopping_cart():
    cart_page = NopCommerceCartPage()
    assert cart_page.shopping_cart() == True
    print("Cart details are verified!")

# Test case for validating the removal of a product from the cart.
def test_remove_cart_product():
    cart_page = NopCommerceCartPage()
    assert cart_page.remove_cart_product() == True
    print("Product successfully removed from cart!")




