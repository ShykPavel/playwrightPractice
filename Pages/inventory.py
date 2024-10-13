from playwright.sync_api import Page

class InventoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.shopping_cart_icon = page.locator("[data-test=\"shopping-cart-link\"]")
        self.sorting_options_dropdown = page.locator(("[data-test=\"product-sort-container\"]"))
        self.inventory_items = page.locator(".inventory_item")
        self.menu_button = page.get_by_role("button", name="Open Menu")
        self.close_menu_button = page.get_by_role("button", name="Close Menu")


    def select_item_by_index(self, index = int):
        return self.inventory_items.nth(index).first

    def add_item_to_chart_by_index(self, index):
        item = self.select_item_by_index(index)
        add_to_cart_button = item.locator("[data-test^=\"add-to-cart-\"]")
        add_to_cart_button.click()

    def remove_item_from_chart_by_index(self, index):
        item = self.select_item_by_index(index)
        remove_from_cart_button = item.locator("[data-test^=\"remove-\"]")
        remove_from_cart_button.click()

    def get_item_name_by_index(self, index):
        return self.page.locator(".inventory_item_name").nth(index).text_content()

    def get_item_price_by_index(self, index):
        return self.page.locator(".inventory_item_price").nth(index).text_content()
