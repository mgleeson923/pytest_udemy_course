from ssqaapitest.src.utlities.requestUtilities import RequestUtilities


class ProductHelper(object):

    def __init__(self):
        self.requests_utility = RequestUtilities()

    def get_products_by_id(self, product_id):
        return self.requests_utility.get(f"products/{product_id}")
