import pytest
from ssqaapitest.src.utlities.genericUtilities import generate_random_string
from ssqaapitest.src.helpers.product_helper import ProductHelper
from ssqaapitest.src.dao.products_dao import ProductsDAO

pytestmark = [pytest.mark.products, pytest.mark.smoke]


@pytest.mark.tcid26
def test_create_one_simple_product():
    # Generate Data
    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = "simple"
    payload['regular_price'] = "10.99"

    # Make API call
    product_rs = ProductHelper().call_create_product(payload)

    # Verify Response is not Empty
    assert product_rs, f"Create product API Response is Empty. Payload: {payload}"
    assert product_rs['name'] == payload['name']
    f"Create product API Call response has" \
    f"unexpected name. Expected: {payload['name']}, Actual: {product_rs['name']}"

    # Verify Product in Database
    product_id = product_rs['id']
    db_product = ProductsDAO().get_product_by_id(product_id)

    assert payload['name'] == db_product[0]['post_title']
    f"Product Name in DB does not match Product Name in API" \
    f"DB: {db_product[0]['post_title']}, API:{payload['name']}"
