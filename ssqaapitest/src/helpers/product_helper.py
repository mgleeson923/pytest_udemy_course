from ssqaapitest.src.utlities.requestUtilities import RequestUtilities
import logging as logger


class ProductHelper(object):

    def __init__(self):
        self.requests_utility = RequestUtilities()

    def get_products_by_id(self, product_id):
        return self.requests_utility.get(f"products/{product_id}")

    def call_create_product(self, payload):
        return self.requests_utility.post('products', payload=payload, expected_status_code=201)

    def call_list_products(self, payload=None):

        max_pages = 1000
        all_products = []
        for i in range(1, max_pages + 1):
            logger.debug(f"List Products Page Number: {i}")

            if not 'per_page' in payload.keys():
                payload['per_page'] = 100

            # Add current Page Number to Call
            payload['page'] = i
            rs_api = self.requests_utility.get('products', payload=payload)

            # If there is no response then stop the loop b/c there are no more products
            if not rs_api:
                break
            else:
                all_products.extend(rs_api)
        else:
            raise Exception(f"Unable to find all Products after {max_pages} pages")

        return all_products
