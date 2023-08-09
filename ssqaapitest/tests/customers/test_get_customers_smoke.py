import logging as logger
import pytest
from ssqaapitest.src.utlities.requestUtilities import RequestUtilities


@pytest.mark.tcid30
def test_get_all_customers():
    req_helper = RequestUtilities()
    rs_api = req_helper.get('customers')

    assert rs_api, f"Response of list all customers is empty"
