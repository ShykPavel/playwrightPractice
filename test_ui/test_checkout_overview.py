from random import randint

from playwright.sync_api import expect


def test_confirm_checkout(logged_in_page, inventory_page, cart_page, checkout_information, checkout_overview, checkout_complete):
    logged_in_page.wait_for_load_state()
    inventory_page.add_item_to_chart_by_index(0)
    item_added = inventory_page.get_item_name_by_index(0)
    inventory_page.shopping_cart_icon.click()
    cart_page.page.wait_for_load_state()
    cart_page.checkout_button.click()
    checkout_information.enter_first_name(checkout_information.valid_first_name)
    checkout_information.enter_last_name(checkout_information.valid_last_name)
    checkout_information.enter_postal_code(checkout_information.valid_postal_code)
    checkout_information.continue_button.click()
    assert checkout_overview.inventory_items.count() == 1, "Item's quantity doesn't match"
    assert checkout_overview.get_item_name_by_index(0) == item_added, "Added item doesn't match"
    checkout_overview.finish_button.click()
    checkout_overview.page.wait_for_load_state()
    expect(checkout_complete.checkout_complete_header, "Checkout complete screen is not opened").to_be_visible()
    assert checkout_complete.page.url == "https://www.saucedemo.com/checkout-complete.html", "URL doesn't match"

def test_items_total_price(logged_in_page, inventory_page, cart_page, checkout_information, checkout_overview, checkout_complete):
    logged_in_page.wait_for_load_state()
    inventory_items_count = inventory_page.inventory_items.count()
    items_amount_added = 0
    for i in range(randint(0,inventory_items_count)):
        inventory_page.add_item_to_chart_by_index(i)
        items_amount_added += 1
    item_inventory_prices = []
    for i in range(inventory_page.inventory_items.count()):
        remove_button = inventory_page.inventory_items.nth(i).locator("[data-test^='remove-']")
        if remove_button.is_visible():
            item_price = inventory_page.get_item_price_by_index(i).replace("$", "")
            item_inventory_prices.append(float(item_price))
    inventory_page.shopping_cart_icon.click()
    cart_page.page.wait_for_load_state()
    cart_page.checkout_button.click()
    checkout_information.enter_first_name(checkout_information.valid_first_name)
    checkout_information.enter_last_name(checkout_information.valid_last_name)
    checkout_information.enter_postal_code(checkout_information.valid_postal_code)
    checkout_information.continue_button.click()
    assert checkout_overview.inventory_items.count() == items_amount_added, "Item's quantity doesn't match"
    total_price_calculated = round(sum(item_inventory_prices) + float(checkout_overview.tax_label.text_content().replace("$","").replace("Tax: ","")), 2)
    total_price_label_value = float(checkout_overview.total_label.text_content().replace("Total: $",""))
    assert total_price_calculated == total_price_label_value

def test_cancel_button_action (logged_in_page, inventory_page, cart_page, checkout_information, checkout_overview):
    logged_in_page.wait_for_load_state()
    inventory_page.add_item_to_chart_by_index(0)
    inventory_page.shopping_cart_icon.click()
    cart_page.page.wait_for_load_state()
    cart_page.checkout_button.click()
    checkout_information.enter_first_name(checkout_information.valid_first_name)
    checkout_information.enter_last_name(checkout_information.valid_last_name)
    checkout_information.enter_postal_code(checkout_information.valid_postal_code)
    checkout_information.continue_button.click()
    checkout_overview.cancel_button.click()
    expect(inventory_page.inventory_items.first, "Inventory is not visible").to_be_visible()
    assert inventory_page.page.url == "https://www.saucedemo.com/inventory.html", "URL doesn't match"