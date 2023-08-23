import pytest
from ssqaapitest.src.utlities.requestUtilities import RequestUtilities
from ssqaapitest.src.dao.products_dao import ProductsDAO
from ssqaapitest.src.helpers.product_helper import ProductHelper


@pytest.mark.products
@pytest.mark.tcid24
def test_get_all_products():
    req_helper = RequestUtilities()
    rs_api = req_helper.get(endpoint='products')
    assert rs_api, f"Get All Products Endpoint Returned Empty"


@pytest.mark.products
@pytest.mark.tcid25
def test_get_product_by_id():
    # Get a Product from the Database
    rand_product = ProductsDAO().get_random_product_from_db(1)
    rand_product_id = rand_product[0]['ID']
    db_name = rand_product[0]['post_title']

    # Make Call to API
    product_helper = ProductHelper()
    rs_api = product_helper.get_products_by_id(rand_product_id)
    api_name = rs_api['name']

    # Verify Response
    assert db_name == api_name, f"Get Product by ID Returned Wrong Product. ID: {rand_product_id}" \
                                f"DB Name: {db_name}, API NAME: {api_name}"

