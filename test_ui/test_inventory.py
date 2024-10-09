from Pages.inventory import InventoryPage
from Pages.login_page import LoginPage

def test_adding_item_to_cart(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    logged_in_page.wait_for_load_state()
    inventory.add_item_to_chart_by_index(0)
    print("hell yeah!")
