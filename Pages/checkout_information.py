from playwright.sync_api import Page

class CheckoutInformation:

    valid_first_name = "Pavel"
    valid_last_name = "Shyk"
    valid_postal_code = "01-636"

    def __init__(self, page: Page):
        self.page = page
        self.first_name_field = page.locator("[data-test=\"firstName\"]")
        self.last_name_field = page.locator("[data-test=\"lastName\"]")
        self.postal_code_field = page.locator("[data-test=\"postalCode\"]")
        self.continue_button = page.locator("[data-test=\"continue\"]")
        self.cancel_button = page.locator("[data-test=\"cancel\"]")
        self.error_message = page.locator("class=error-message-container error")
        self.close_error_message_button = page.locator("[data-test=\"error-button\"]")

    def enter_first_name (self, first_name = str):
        self.first_name_field.fill(first_name)

    def enter_last_name (self, last_name = str):
        self.last_name_field.fill(last_name)

    def enter_postal_code (self, postal_code = str):
        self.postal_code_field.fill(postal_code)
