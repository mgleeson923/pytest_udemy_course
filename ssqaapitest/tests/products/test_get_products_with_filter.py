import pytest
from datetime import datetime, timedelta
from ssqaapitest.src.helpers.product_helper import ProductHelper
from ssqaapitest.src.dao.products_dao import ProductsDAO

import pdb


@pytest.mark.regression
class TestListProductsWithFilter(object):

    @pytest.mark.tcid51
    def test_list_products_with_filter_after(self):
        # Create Test Data
        x_days_from_today = 300
        _after_created_date = datetime.now().replace(microsecond=0) - timedelta(days=x_days_from_today)
        after_created_date = _after_created_date.isoformat()

        # Make API Call
        payload = dict()
        payload['after'] = after_created_date
        rs_api = ProductHelper().call_list_products(payload)
        assert rs_api, f"Empty Response for 'List Products with Filter'"

        # Get Data from Database
        db_products = ProductsDAO().get_products_created_after_given_date(after_created_date)

        # Verify Response
        assert len(rs_api) == len(db_products), f"List of Products with Filter 'After' returned unexpected number " \
                                                f"of products. Expected: {len(db_products)}, Actual: {len(rs_api)}"

        ids_in_api = [i['id'] for i in rs_api]
        ids_in_db = [i['ID'] for i in db_products]

        ids_diff = list(set(ids_in_api) - set(ids_in_db))

        assert not ids_diff, f"List Products with Filter. Products IDs in Response Do Not Match."
