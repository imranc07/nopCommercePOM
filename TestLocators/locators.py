"""
Locators file contains all the web locators like XPATH, class NAME, ID, link text etc

"""

class NopCommerceLocators:

    # Locatores for Registration Page and Login Page
    registration_menu = 'ico-register' # Class Locator
    gender_button = 'gender-male' # ID Locator
    firstname_locator = 'FirstName' # ID Locator
    lastname_locator = 'LastName' # ID Locator
    dob_day = '//*[@id="main"]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[1]' # XPATH Locator
    dob_month = '//*[@id="main"]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[2]' # XPATH Locator
    dob_year = '//*[@id="main"]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[3]' # XPATH Locator
    email_locator = 'Email' # ID Locator
    password_locator = 'Password' # ID Locator
    confirm_password_locator = 'ConfirmPassword' # ID Locator
    register_button = 'register-button' # ID Locator
    success_message = '//*[@id="main"]/div/div/div/div[2]/div[1]' #XPATH Locator
    error_message = 'field-validation-error' # Class Locator
    continue_button = '//*[@id="main"]/div/div/div/div[2]/div[2]/a' #XPATH
           
    # Locators for Login Page
    login_menu = 'ico-login' # Class Locator
    rememberme_checkbox = 'RememberMe' # ID Locator
    login_button = '//*[@id="main"]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button' # XPATH Locator
    myaccount_locator = 'ico-account' # Class Locator
    login_error_message = '//*[@id="main"]/div/div/div/div[2]/div[1]/div[2]/form/div[1]' # XPATH Locator
    wrong_email_message = '//*[@id="Email-error"]' #XPATH locator

    # Locators for logout
    logout_button = '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a' # XPATH Locator

    # Locators for Product Page
    search_box = 'small-searchterms' #ID Locator
    search_button = '//*[@id="small-search-box-form"]/button' # XPATH locator
    sortby_locaor = 'products-orderby' # ID Locator
    product_locator = '//*[@id="main"]/div/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div/div[2]/h2/a' # XPATH Locator
    product_text = '//*[@id="product-details-form"]/div/div[1]/div[2]/div[1]/h1' # XPATH Locator

    # Locators for Cart Page
    shopping_cart_menu = '//*[@id="topcartlink"]/a' # XPATH Locator
    cart_total = '//*[@id="shopping-cart-form"]/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[2]/span/strong' # XPATH Locator
    remove_button = '//*[@id="shopping-cart-form"]/div[1]/table/tbody/tr/td[7]/button' # XPATH Locator
    empty_cart_text = '//*[@id="main"]/div/div/div/div[2]/div/div' # XPATH Locator
    add_card_success_message = '//*[@id="bar-notification"]/div/p' # XPATH Locator
    select_any_product = '//*[@id="main"]/div/div/div/div/div[4]/div[2]/div[3]/div/div[2]/div[3]/div[2]/button[1]' # XPATH Locator
    add_cart = '//*[@id="add-to-cart-button-18"]' # XPATH Locator

    # Locators for Checkout Page
    terms_checkbox = 'termsofservice' # ID Locator
    checkout_button = 'checkout' # ID Locator
    country_locator = 'BillingNewAddress_CountryId' # ID Locator 
    city_locator = 'BillingNewAddress_City' # ID Locator
    address_line1 = 'BillingNewAddress_Address1' # ID Locator
    postal_code_locator = 'BillingNewAddress_ZipPostalCode' # ID Locator
    phone_number_locator = 'BillingNewAddress_PhoneNumber' # ID Locator
    checkout_continue_button = '//*[@id="billing-buttons-container"]/button[2]' # XPATH Locator
    shipping_continue_button = '//*[@id="shipping-method-buttons-container"]/button' # XPATH Locator
    payment_continue_button = '//*[@id="payment-method-buttons-container"]/button' # XPATH Locator
    payment_info_continue_button = '//*[@id="payment-info-buttons-container"]/button' # XPATH Locator
    confrim_button = '//*[@id="confirm-order-buttons-container"]/button' # XPATH Locator
    confirm_order_success_message = '//*[@id="main"]/div/div/div/div[2]/div/div[1]/strong' # XPATH Locator "Your order has been successfully processed!"
    order_ID_text = '//*[@id="main"]/div/div/div/div[2]/div/div[2]/div[1]/strong' # XPATH Locator
