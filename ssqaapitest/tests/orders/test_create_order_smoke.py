import pytest
from ssqaapitest.src.dao.products_dao import ProductsDAO
from ssqaapitest.src.helpers.orders_helper import OrdersHelper


@pytest.mark.tcid48
def test_create_paid_order_guest_user():
    product_dao = ProductsDAO()
    order_helper = OrdersHelper()

    # Get a Product from DB
    rand_product = product_dao.get_random_product_from_db(1)
    product_id = rand_product[0]['ID']

    # Make API Call
    order_helper.create_order()

    # Verify Response

    # Verify Database
