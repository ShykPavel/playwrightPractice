from playwright.sync_api import Page

class CheckoutComplete:

    def __init__(self, page: Page):
        self.page = page
        self.back_to_inventory_button = page.locator("[data-test=\"back-to-products\"]")
        self.checkout_complete_image = page.locator("[data-test=\"pony-express\"]")
        self.checkout_complete_header = page.locator("[data-test=\"complete-header\"]")
        self.checkout_complete_text = page.locator("[data-test=\"complete-text\"]")
