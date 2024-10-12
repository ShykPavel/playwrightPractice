from playwright.sync_api import expect


def test_fill_all_order_data(logged_in_page, inventory_page, cart_page, checkout_information, checkout_overview):
    logged_in_page.wait_for_load_state()
    inventory_page.add_item_to_chart_by_index(0)
    inventory_page.shopping_cart_icon.click()
    cart_page.page.wait_for_load_state()
    cart_page.checkout_button.click()
    checkout_information.enter_first_name(checkout_information.valid_first_name)
    checkout_information.enter_last_name(checkout_information.valid_last_name)
    checkout_information.enter_postal_code(checkout_information.valid_postal_code)
    checkout_information.continue_button.click()
    expect(checkout_overview.finish_button, "Checkout overview screen in not open").to_be_visible()
    assert checkout_information.page.url == "https://www.saucedemo.com/checkout-step-two.html"

def test_checkout_without_filled_data(logged_in_page, inventory_page, cart_page, checkout_information, checkout_overview):
    logged_in_page.wait_for_load_state()
    inventory_page.add_item_to_chart_by_index(0)
    inventory_page.shopping_cart_icon.click()
    cart_page.page.wait_for_load_state()
    cart_page.checkout_button.click()
    checkout_information.continue_button.click()
    expect(checkout_overview.finish_button, "It's possible to continue checkout w\o personal info").not_to_be_visible()
    assert checkout_information.page.url == "https://www.saucedemo.com/checkout-step-one.html"

def test_cancel_button (logged_in_page, inventory_page, cart_page, checkout_information, checkout_overview):
    logged_in_page.wait_for_load_state()
    inventory_page.add_item_to_chart_by_index(0)
    inventory_page.shopping_cart_icon.click()
    cart_page.page.wait_for_load_state()
    cart_page.checkout_button.click()
    checkout_information.cancel_button.click()
    expect(cart_page.cart_item, "Cart page is not opened").to_be_visible()
    assert inventory_page.page.url == "https://www.saucedemo.com/cart.html", "URL doesn't match"