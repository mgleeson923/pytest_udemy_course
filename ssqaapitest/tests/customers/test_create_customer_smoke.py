
import pytest
import logging as logger
from ssqaapitest.src.utlities.genericUtilities import generate_random_email_and_password



@pytest.mark.tcid29
def test_create_customer_only_email_password():

    logger.info("Test: Create New Customer with Email and Password Only")

    rand_info = generate_random_email_and_password()

    email = rand_info['email']
    password = rand_info['password']

    # create payload
    payload = {'email': email, 'password': password}

    # make call

    # verify status code

    # verify email in response

    # verify customer is created in database
