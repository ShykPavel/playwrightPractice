from Pages.inventory import InventoryPage
from Pages.login_page import LoginPage

def test_adding_item_to_cart(page):
    login_page = LoginPage(page)
    inventory = InventoryPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.login_button.click()
    page.wait_for_load_state()
    inventory.add_item_to_chart_by_index(0)
    print("hell yeah!")
