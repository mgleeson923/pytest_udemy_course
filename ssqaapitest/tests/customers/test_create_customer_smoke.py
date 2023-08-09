import pytest
import logging as logger
from ssqaapitest.src.utlities.genericUtilities import generate_random_email_and_password
from ssqaapitest.src.helpers.customer_helper import CustomerHelper
from ssqaapitest.src.dao.customer_dao import Customer_DAO
from ssqaapitest.src.utlities.requestUtilities import RequestUtilities


@pytest.mark.customers
@pytest.mark.tcid29
def test_create_customer_only_email_password():
    logger.info("Test: Create New Customer with Email and Password Only")

    rand_info = generate_random_email_and_password()

    email = rand_info['email']
    password = rand_info['password']

    # create payload
    payload = {'email': email, 'password': password}

    # make call
    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password)

    # verify status code & customer name & email
    assert cust_api_info['email'] == email, f"Create Customer API Return Wrong Email. Email:{email}"
    assert cust_api_info['first_name'] == '', f"Create Customer API returned value for firstname, but should be empty."

    # verify customer is created in database
    cust_dao = Customer_DAO()
    cust_info = cust_dao.get_customer_by_email(email)

    id_in_api = cust_api_info['id']
    id_in_db = cust_info[0]['ID']
    assert id_in_api == id_in_db, f'Create Customer Response ID not same as ID in Database' \
                                  f'Email: {email}'


@pytest.mark.customers
@pytest.mark.tcid47
def test_create_customer_fail_for_existing_email():
    # get existing email from Database
    cust_dao = Customer_DAO()
    existing_cust = cust_dao.get_random_customer_from_db()
    existing_email = existing_cust[0]['user_email']

    # Make API call
    req_helper = RequestUtilities()
    payload = {"email": existing_email, "password": "Password1"}
    cust_api_info = req_helper.post(endpoint='customers', payload=payload, expected_status_code=400)

    assert cust_api_info['code'] == 'registration-error-email-exists', f"Create Customer with existing" \
    f"email error 'code' is not correct. Expected: registration-error-email-exists, Actual: {cust_api_info['code']}"

    assert cust_api_info['message'] == 'An account is already registered with your email address. <a href="#" class="showlogin">Please log in.</a>', \
        f"Actual: {cust_api_info['message']}"
