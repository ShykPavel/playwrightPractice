from playwright.sync_api import Page

class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.cart_item = page.locator("[data-test=\"inventory-item\"]")
        self.cart_counter_badge = page.locator(".shopping_cart_badge")
        self.continue_shipping_button = page.locator("[data-test=\"continue-shopping\"]")
        self.checkout_button = page.locator("[data-test=\"checkout\"]")


    def remove_item_by_index(self, index = int):
        item = self.cart_item.nth(index)
        remove_button = item.locator("[data-test^=\"remove-\"]")
        remove_button.click()

    def get_item_by_index(self, index = int):
        return self.cart_item.nth(index)

    def get_items_quantity(self) -> int:
        items_counter = int(self.cart_counter_badge.text_content())
        return items_counter

    def get_item_name_by_index(self, index):
        return self.page.locator(".inventory_item_name").nth(index).text_content()
