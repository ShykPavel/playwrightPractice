from playwright.sync_api import expect


def test_checkout_complete(logged_in_page, inventory_page, cart_page, checkout_information, checkout_overview, checkout_complete):
    logged_in_page.wait_for_load_state()
    inventory_page.add_item_to_chart_by_index(0)
    inventory_page.shopping_cart_icon.click()
    cart_page.page.wait_for_load_state()
    cart_page.checkout_button.click()
    checkout_information.enter_first_name(checkout_information.valid_first_name)
    checkout_information.enter_last_name(checkout_information.valid_last_name)
    checkout_information.enter_postal_code(checkout_information.valid_postal_code)
    checkout_information.continue_button.click()
    checkout_overview.finish_button.click()
    checkout_overview.page.wait_for_load_state()
    expect(checkout_complete.checkout_complete_header, "Checkout complete screen is not opened").to_be_visible()
    expect(checkout_complete.checkout_complete_image, "Checkout complete screen is not opened").to_be_visible()
    expect(checkout_complete.checkout_complete_text, "Checkout complete screen is not opened").to_be_visible()
    assert checkout_complete.page.url == "https://www.saucedemo.com/checkout-complete.html", "URL doesn't match"

def test_checkout_complete_back_home_button(logged_in_page, inventory_page, cart_page, checkout_information, checkout_overview, checkout_complete):
    logged_in_page.wait_for_load_state()
    inventory_page.add_item_to_chart_by_index(0)
    inventory_page.shopping_cart_icon.click()
    cart_page.page.wait_for_load_state()
    cart_page.checkout_button.click()
    checkout_information.enter_first_name(checkout_information.valid_first_name)
    checkout_information.enter_last_name(checkout_information.valid_last_name)
    checkout_information.enter_postal_code(checkout_information.valid_postal_code)
    checkout_information.continue_button.click()
    checkout_overview.finish_button.click()
    checkout_overview.page.wait_for_load_state()
    checkout_complete.back_to_inventory_button.click()
    expect(inventory_page.inventory_items.first, "Inventory is not visible").to_be_visible()
    assert inventory_page.page.url == "https://www.saucedemo.com/inventory.html", "URL doesn't match"
