import pytest

from Pages.inventory import InventoryPage
from Pages.login_page import LoginPage
from Pages.cart import CartPage



@pytest.fixture(scope="function")
def logged_in_page(page):
    login_page = LoginPage(page)
    page.goto(login_page.log_in_page_url)
    login_page.enter_username(login_page.valid_username)
    login_page.enter_password(login_page.valid_password)
    login_page.login_button.click()

    yield page


@pytest.fixture
def cart_page(logged_in_page):
    return CartPage(logged_in_page)

@pytest.fixture
def inventory_page(logged_in_page):
    return InventoryPage(logged_in_page)
