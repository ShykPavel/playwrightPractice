from time import sleep

from playwright.sync_api import expect

from Pages.cart import CartPage
from Pages.inventory import InventoryPage
from Pages.login_page import LoginPage

def test_adding_item_to_cart(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)
    logged_in_page.wait_for_load_state()
    inventory.add_item_to_chart_by_index(0)
    item_inventory_name =  inventory.get_item_name_by_index(0)
    inventory.shopping_cart_icon.click()
    item_chart_name = cart.get_item_name_by_index(0)
    assert item_inventory_name == item_chart_name, "item is not added to cart"


def test_removing_item_from_cart(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)
    logged_in_page.wait_for_load_state()
    inventory.add_item_to_chart_by_index(0)
    inventory.remove_item_from_chart_by_index(0)
    inventory.shopping_cart_icon.click()
    cart.page.wait_for_load_state()
    expect(cart.cart_item, "Item is not removed").to_be_hidden()