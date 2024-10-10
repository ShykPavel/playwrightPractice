from playwright.sync_api import Page

class CheckoutInformation:

    def __init__(self, page: Page):
        self.page = page
        self.first_name_field = page.locator("[data-test=\"firstName\"]")
        self.last_name_field = page.locator("[data-test=\"lastName\"]")
        self.postal_code_field = page.locator("[data-test=\"postalCode\"]")
        self.continue_button = page.locator("[data-test=\"continue\"]")
        self.cancel_button = page.locator("[data-test=\"cancel\"]")
        self.error_message = page.locator("class=error-message-container error")
        self.close_error_message_button = page.locator("[data-test=\"error-button\"]")
