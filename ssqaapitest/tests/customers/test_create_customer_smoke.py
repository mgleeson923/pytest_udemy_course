
import pytest
import logging as logger
from ssqaapitest.src.utlities.genericUtilities import generate_random_email_and_password
from ssqaapitest.src.helpers.customer_helper import CustomerHelper



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

    import pdb; pdb.set_trace()

    # verify status code

    # verify email in response

    # verify customer is created in database
