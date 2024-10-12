from random import randint

from playwright.sync_api import expect



def test_checkout_option_with_item_added(logged_in_page, inventory_page, cart_page, checkout_information):
    logged_in_page.wait_for_load_state()
    inventory_page.add_item_to_chart_by_index(0)
    inventory_page.shopping_cart_icon.click()
    cart_page.page.wait_for_load_state()
    cart_page.checkout_button.click()
    expect(checkout_information.first_name_field, "Checkout information is not visible").to_be_visible()

def test_checkout_option_without_item_added(logged_in_page, inventory_page, cart_page, checkout_information):
    logged_in_page.wait_for_load_state()
    inventory_page.shopping_cart_icon.click()
    cart_page.page.wait_for_load_state()
    cart_page.checkout_button.click()
    expect(checkout_information.first_name_field, "Checkout information open for 0 items cart").not_to_be_visible()

def test_remove_items_from_cart(logged_in_page, inventory_page, cart_page, checkout_information):
    logged_in_page.wait_for_load_state()
    inventory_page.add_item_to_chart_by_index(0)
    inventory_page.shopping_cart_icon.click()
    cart_page.remove_item_by_index(0)
    items_in_cart = cart_page.cart_item.count()
    assert items_in_cart == 0, "Item is not removed from cart"


def test_continue_shopping_option_(logged_in_page, inventory_page, cart_page):
    logged_in_page.wait_for_load_state()
    inventory_page.shopping_cart_icon.click()
    cart_page.page.wait_for_load_state()
    cart_page.continue_shipping_button.click()
    expect(inventory_page.inventory_items.first, "Inventory is not visible").to_be_visible()
    assert inventory_page.page.url == "https://www.saucedemo.com/inventory.html", "URL doesn't match"

def test_cart_items_counter(logged_in_page, inventory_page, cart_page):
    logged_in_page.wait_for_load_state()
    inventory_items_count = inventory_page.inventory_items.count()
    items_amount_added = 0
    for i in range(randint(0,inventory_items_count)):
        inventory_page.add_item_to_chart_by_index(i)
        items_amount_added += 1
    inventory_page.shopping_cart_icon.click()
    counter_value = cart_page.get_items_quantity()
    assert items_amount_added == counter_value, "Unexpected value in chart items counter"



