from ssqaapitest.src.utlities.genericUtilities import generate_random_email_and_password
from ssqaapitest.src.utlities.requestUtilities import RequestUtilities


class CustomerHelper(object):

    def __init__(self):
        self.requests_utility = RequestUtilities()

    def create_customer(self, email=None, password=None, **kwargs):

        if not email:
            ep = generate_random_email_and_password()
            email = ep['email']
        if not password:
            password = 'Password1'

        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)

        self.requests_utility.post('customers', payload=payload)

        return True
