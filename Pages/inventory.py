from playwright.sync_api import Page

class InventoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.shopping_cart_icon = page.locator("[data-test=\"shopping-cart-link\"]")
        self.filters_dropdown = page.get_by_text("Name (A to Z)Name (A to Z)")
        self.inventory_items = page.locator(".inventory_item")
        self.menu_button = page.get_by_role("button", name="Open Menu")
        self.close_menu_button = page.get_by_role("button", name="Close Menu")

    def menu_elements(self):
        all_items = self.page.locator("[data-test=\"inventory-sidebar-link\"]")
        about = self.page.locator("[data-test=\"about-sidebar-link\"]")
        logout = self.page.locator("[data-test=\"logout-sidebar-link\"]")
        reset_app_state = self.page.locator("[data-test=\"reset-sidebar-link\"]")

        return all_items, about, logout, reset_app_state

    def select_item_by_index(self, index = int):
        return self.inventory_items.nth(index).first

    def add_item_to_chart_by_index(self, index):
        item = self.select_item_by_index(index)
        add_to_cart_button = item.locator("[data-test^=\"add-to-cart-\"]")
        add_to_cart_button.click()

    def remove_item_from_chart_by_index(self, index):
        item = self.select_item_by_index(index)
        remove_from_cart_button = item.locator("[data-test=\"remove-sauce-labs-backpack\"]")
        remove_from_cart_button.click()

    def get_item_name_by_index(self, index):
        return self.page.locator(".inventory_item_name").nth(index).text_content()
