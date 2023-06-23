# Test with Setup and Teardown

import pytest

pytestmark = [pytest.mark.be, pytest.mark.slow]


@pytest.fixture(scope='module')
def my_setup():
    print("")
    print("<<<<SETUP>>>>")

    return {'id': 20, 'name': 'Mike'}


@pytest.mark.smoke
def test_login_page_valid_user(my_setup):
    print("")
    print("Logging in with valid user")
    print("function: aaaaa")
    print("Name: {}".format(my_setup.get('name')))
    # import pdb; pdb.set_trace()


@pytest.mark.regression
def test_login_page_wrong_password(my_setup):
    print("")
    print("Login with wrong password")
    print("Function: bbbbbbbbb")
