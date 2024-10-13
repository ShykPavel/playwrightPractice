from playwright.sync_api import Page

class CheckoutOverview:

    def __init__(self, page: Page):
        self.page = page
        self.inventory_items = page.locator("[data-test=\"inventory-item\"]")
        self.subtotal_price_label = page.locator("[data-test=\"subtotal-label\"]")
        self.tax_label = page.locator("[data-test=\"tax-label\"]")
        self.total_label = page.locator("[data-test=\"total-label\"]")
        self.finish_button = page.locator("[data-test=\"finish\"]")
        self.cancel_button = page.locator("[data-test=\"cancel\"]")

    def get_item_name_by_index(self, index):
        return str(self.page.locator(".inventory_item_name").nth(index).text_content())