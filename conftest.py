import pytest
from Pages.login_page import LoginPage



@pytest.fixture(scope="function")
def logged_in_page(page):
    login_page = LoginPage(page)
    page.goto(login_page.log_in_page_url)
    login_page.enter_username(login_page.valid_username)
    login_page.enter_password(login_page.valid_password)
    login_page.login_button.click()

    yield page


@pytest.fixture(scope="function")
def login_page(page):
    login_page = LoginPage(page)
    page.goto(login_page.log_in_page_url)

    yield login_page
