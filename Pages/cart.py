from playwright.sync_api import Page

class InventoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.cart_item = page.locator("[data-test=\"inventory-item\"]")
        self.item_quantity_field = page.locator("[data-test=\"item-quantity\"]")
        self.continue_shipping_button = page.locator("[data-test=\"continue-shopping\"]")
        self.checkout_button = page.locator("[data-test=\"checkout\"]")


    def remove_item_by_index(self, index = int):
        item = self.cart_item.nth(index)
        remove_button = item.locator("[data-test=\"remove-\"]")
        remove_button.click()

    def get_items_quantity(self) -> int:
        items_counter = self.page.locator("[data-test=\"shopping-cart-badge\"]").get_attribute()
        return items_counter
