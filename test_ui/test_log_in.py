from Pages.login_page import LoginPage

def test_login_valid(login_page):
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.login_button.click()

