from playwright.sync_api import expect
import os

from Pages.inventory import InventoryPage


def test_valid_user_can_login(login_page):
    inventory = InventoryPage(login_page.page)
    login_page.enter_username(os.getenv("VALID_USERNAME"))
    login_page.enter_password(os.getenv("VALID_PASSWORD"))
    login_page.login_button.click()
    expect(inventory.inventory_items.first, message = "inventory is not visible after login").to_be_visible()

def test_locked_user_can_not_login(login_page):
    login_page.enter_username(os.getenv("LOCKED_USERNAME"))
    login_page.enter_password(os.getenv("VALID_PASSWORD"))
    login_page.login_button.click()
    login_page.page.wait_for_load_state()
    expect(login_page.login_error_message, message = "error message is not displayed").to_be_visible()

def test_user_with_incorrect_password_can_not_login(login_page):
    login_page.enter_username(os.getenv("LOCKED_USERNAME"))
    login_page.enter_password(os.getenv("INVALID_PASSWORD"))
    login_page.login_button.click()
    login_page.page.wait_for_load_state()
    expect(login_page.login_error_message, message = "error message is not displayed").to_be_visible()

def test_user_with_incorrect_username_can_not_login(login_page):
    login_page.enter_username(os.getenv("INVALID_USERNAME"))
    login_page.enter_password(os.getenv("VALID_PASSWORD"))
    login_page.login_button.click()
    login_page.page.wait_for_load_state()
    expect(login_page.login_error_message, message = "error message is not displayed").to_be_visible()

def test_locked_user_error_message_contents(login_page):
    login_page.enter_username(os.getenv("LOCKED_USERNAME"))
    login_page.enter_password(os.getenv("VALID_PASSWORD"))
    login_page.login_button.click()
    login_page.page.wait_for_load_state()
    expect(login_page.login_error_message, message="error message text doesn't match").to_have_text("Epic sadface: Sorry, this user has been locked out.")

def test_general_error_message_contents(login_page):
    login_page.enter_username(os.getenv("VALID_USERNAME"))
    login_page.enter_password(os.getenv("INVALID_PASSWORD"))
    login_page.login_button.click()
    login_page.page.wait_for_load_state()
    expect(login_page.login_error_message, message="error message text doesn't match").to_have_text("Epic sadface: Username and password do not match any user in this service")

    def test_close_button_clears_error_state(login_page):
        login_page.enter_username(os.getenv("VALID_USERNAME"))
        login_page.enter_password(os.getenv("INVALID_PASSWORD"))
        login_page.login_button.click()
        login_page.page.wait_for_load_state()
        login_page.login_error_close_button.click()
        expect(login_page.login_error_message, message="error state is visible").to_be_hidden()