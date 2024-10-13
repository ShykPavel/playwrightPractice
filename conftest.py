import pytest

from Pages.checkout_complete import CheckoutComplete
from Pages.checkout_information import CheckoutInformation
from Pages.checkout_overview import CheckoutOverview
from Pages.inventory import InventoryPage
from Pages.login_page import LoginPage
from Pages.cart import CartPage
import os


@pytest.fixture(scope="function")
def login_page(page):
    login_page = LoginPage(page)
    page.goto(login_page.log_in_page_url)

    return  login_page

@pytest.fixture(scope="function")
def logged_in_page(page):
    login_page = LoginPage(page)
    page.goto(login_page.log_in_page_url)
    login_page.enter_username(os.getenv("VALID_USERNAME"))
    login_page.enter_password(os.getenv("VALID_PASSWORD"))
    login_page.login_button.click()

    yield page


@pytest.fixture
def cart_page(logged_in_page):
    return CartPage(logged_in_page)

@pytest.fixture
def inventory_page(logged_in_page):
    return InventoryPage(logged_in_page)

@pytest.fixture
def cart_page(logged_in_page):
    return CartPage(logged_in_page)

@pytest.fixture
def checkout_information(logged_in_page):
    return CheckoutInformation(logged_in_page)

@pytest.fixture
def checkout_overview(logged_in_page):
    return CheckoutOverview(logged_in_page)

@pytest.fixture
def checkout_complete(logged_in_page):
    return CheckoutComplete(logged_in_page)