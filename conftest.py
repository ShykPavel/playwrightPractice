import pytest
from Pages.login_page import LoginPage



@pytest.fixture(scope="function")
def logged_in_page(page):
    login_page = LoginPage(page)
    page.goto(login_page.log_in_page_url)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.login_button.click()

    yield logged_in_page


@pytest.fixture(scope="function")
def login_page(page):
    login_page = LoginPage(page)
    page.goto(login_page.log_in_page_url)

    yield login_page
