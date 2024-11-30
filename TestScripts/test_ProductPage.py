"""
test_ProductPage.py contains the test cases for Product Page.

Test Scripts File
"""

from PageObject.ProductPage import NopCommerceProductPage

# test case for product search, sortby and verfying product details
def test_search_and_brows_product():
    product_page = NopCommerceProductPage()
    product_page.start()
    assert product_page.search_and_brows_product() == True
    print("Success: Product searched, sortby and product details verified!")
