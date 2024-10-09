from playwright.sync_api import Page

class LoginPage:

    log_in_page_url = "https://www.saucedemo.com/"
    valid_username = "standard_user"
    locked_username = "locked_out_user"
    invalid_username = "mistake"
    valid_password = "secret_sauce"
    invalid_password = "mistake"


    def __init__(self, page: Page):
        self.page = page
        self.username_field = page.locator("[data-test=\"username\"]")
        self.password_field = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-button\"]")
        self.login_error_message = page.locator("[data-test=\"error\"]")
        self.login_error_close_button = page.locator("[data-test=\"error-button\"]")


    def enter_username (self, username = str):
        self.username_field.fill(username)

    def enter_password (self, password = str):
        self.password_field.fill(password)

    def click_login (self):
        self.login_button.click()

    def close_error_message(self):
        self.login_error_close_button.click()



