import os


class CredentialUtility(object):

    def __init__(self):
        pass

    @staticmethod
    def get_wc_api_keys():

        wc_key = os.environ.get('WC_KEY')
        wc_secret = os.environ.get('WC_SECRET')

        if not wc_key or not wc_secret:
            raise Exception("API Credentials must be set in ENV File")
        else:
            return {'wc_key': wc_key, 'wc_secret': wc_secret}
