from playwright.sync_api import expect

def test_adding_item_to_cart(logged_in_page,cart_page, inventory_page):
    logged_in_page.wait_for_load_state()
    inventory_page.add_item_to_chart_by_index(0)
    item_inventory_name =  inventory_page.get_item_name_by_index(0)
    inventory_page.shopping_cart_icon.click()
    item_chart_name = cart_page.get_item_name_by_index(0)
    assert item_inventory_name == item_chart_name, "item is not added to cart"

def test_add_multiple_items_to_cart(logged_in_page, cart_page,inventory_page):
    logged_in_page.wait_for_load_state()
    item_inventory_names = []
    for i in range(inventory_page.inventory_items.count()):
        inventory_page.add_item_to_chart_by_index(i)
        item_inventory_names.append(inventory_page.get_item_name_by_index(i))
    inventory_page.shopping_cart_icon.click()
    item_chart_names = []
    for i in range(cart_page.cart_item.count()):
        item_chart_names.append(cart_page.get_item_name_by_index(i))
    assert item_inventory_names == item_chart_names, "item is not added to cart"


def test_removing_item_from_cart(logged_in_page, cart_page, inventory_page):
    inventory_page.add_item_to_chart_by_index(0)
    inventory_page.remove_item_from_chart_by_index(0)
    expect(inventory_page.page.locator("[data-test^=\"remove-\"]"), "Remove button persists on the screen").not_to_be_visible()
    inventory_page.shopping_cart_icon.click()
    cart_page.page.wait_for_load_state()
    expect(cart_page.cart_item, "Item is not removed").to_be_hidden()

def test_remove_multiple_items_to_cart(logged_in_page, cart_page,inventory_page):
    logged_in_page.wait_for_load_state()
    item_inventory_names = []
    for i in range(inventory_page.inventory_items.count()):
        inventory_page.add_item_to_chart_by_index(i)
        item_inventory_names.append(inventory_page.get_item_name_by_index(i))
    for i in range(inventory_page.inventory_items.count()):
        inventory_page.remove_item_from_chart_by_index(i)
    item_chart_names = []
    inventory_page.shopping_cart_icon.click()
    for i in range(cart_page.cart_item.count()):
        item_chart_names.append(cart_page.get_item_name_by_index(i))
    assert not item_inventory_names == item_chart_names, "items are not removed from cart"

def test_default_az_sorting_option(logged_in_page, inventory_page):
    default_sorting = inventory_page.sorting_options_dropdown.locator("option:checked").text_content()
    assert default_sorting == "Name (A to Z)", "Default sorting option doesn't match"
    item_inventory_names = []
    for i in range(inventory_page.inventory_items.count()):
        item_inventory_names.append(inventory_page.get_item_name_by_index(i))
    assert item_inventory_names == sorted(item_inventory_names), "Items are not sorted from A-Z"

def test_za_sorting_option(logged_in_page, inventory_page):
    inventory_page.sorting_options_dropdown.select_option("za")
    item_inventory_names = []
    for i in range(inventory_page.inventory_items.count()):
        item_inventory_names.append(inventory_page.get_item_name_by_index(i))
    assert item_inventory_names == sorted(item_inventory_names, reverse = True), "Items are not sorted from Z-A"

def test_price_ascending_sorting_option(logged_in_page, inventory_page):
    inventory_page.sorting_options_dropdown.select_option("lohi")
    item_inventory_prices = []
    for i in range(inventory_page.inventory_items.count()):
        item_inventory_prices.append(float(inventory_page.get_item_price_by_index(i).replace("$","")))
    assert item_inventory_prices == sorted(item_inventory_prices), "Items are not sorted by price from low to high"

def test_price_descending_sorting_option(logged_in_page, inventory_page):
    inventory_page.sorting_options_dropdown.select_option("hilo")
    item_inventory_prices = []
    for i in range(inventory_page.inventory_items.count()):
        item_inventory_prices.append(float(inventory_page.get_item_price_by_index(i).replace("$","")))
    assert item_inventory_prices == sorted(item_inventory_prices, reverse = True), "Items are not sorted by price from high to low"