import pytest
import logging as logger
from ssqaapitest.src.utlities.genericUtilities import generate_random_email_and_password
from ssqaapitest.src.helpers.customer_helper import CustomerHelper
from ssqaapitest.src.dao.customer_dao import Customer_DAO


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

    import pdb;
    pdb.set_trace()
