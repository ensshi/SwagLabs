from pages.home_page import HomePage 
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_information_page import CheckoutInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage


def test_Swag_Labs(driver):
    home_page = HomePage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_information_page = CheckoutInformationPage(driver)
    checkout_overview_page = CheckoutOverviewPage(driver)
    checkout_complete_page = CheckoutCompletePage(driver)

    home_page.go_to()
    home_page.login('standard_user','secret_sauce')
    products_page.is_login_button_invisible()
    assert products_page.get_products_title() == 'Products'

    products_page.add_to_cart('add-to-cart-sauce-labs-fleece-jacket')
    products_page.add_to_cart('add-to-cart-sauce-labs-backpack')
    products_page.click_cart_link()

    cart_page.is_products_title_invisible()
    assert cart_page.get_your_cart_title() == 'Your Cart'

    item_names = cart_page.get_item_names()
    assert len(item_names) == 2 
    assert "Sauce Labs Backpack" in item_names  
    assert "Sauce Labs Fleece Jacket" in item_names
    cart_page.checkout()

    assert checkout_information_page.get_checkout_title() == 'Checkout: Your Information'

    checkout_information_page.form_fill('Ime','Prezime','71000')
    checkout_information_page.continue_button()

    assert checkout_overview_page.get_overview_title() == 'Checkout: Overview'
    item_names = checkout_overview_page.get_item_names()
    assert len(item_names) == 2 
    assert "Sauce Labs Backpack" in item_names  
    assert "Sauce Labs Fleece Jacket" in item_names
    checkout_overview_page.finish_button()

    assert checkout_complete_page.get_complete_title() == 'Checkout: Complete!'

    checkout_complete_page.menu_icon_click()
    checkout_complete_page.logout()

    assert home_page.get_login_logo() == 'Swag Labs'
