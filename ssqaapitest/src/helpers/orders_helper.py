import os
import json
import pdb

class OrdersHelper(object):

    def __init__(self):
        # Gets path of current file
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))
        pass

    def create_order(self, additional_args=None):

        # Finds the path from the current file to the Data JSON File
        payload_template = os.path.join(self.cur_file_dir, '..', 'data', 'create_order_payload.json')

        with open(payload_template) as f:
            payload = json.load(f)

            pdb.set_trace()