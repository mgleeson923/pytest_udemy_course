import pytest


@pytest.mark.smoke
def test_login_page_valid_user():
    print("Logging in with valid user")
    print("function: aaaaa")


@pytest.mark.regression
def test_login_page_wrong_password():
    print("Login with wrong password")
    print("Function: bbbbbbbbb")
