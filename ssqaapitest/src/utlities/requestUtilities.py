import requests
from ssqaapitest.src.configs.hosts_config import API_HOSTS
import os
import json
from requests_oauthlib import OAuth1
from ssqaapitest.src.utlities.credentialsUtilities import CredentialUtility
import logging as logger


class RequestUtilities(object):

    def __init__(self):
        pass

        wc_creds = CredentialUtility.get_wc_api_keys()

        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]

        self.auth = OAuth1(wc_creds['wc_key'], wc_creds['wc_secret'])

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad Status Code." \
                                                              f"Expected {self.expected_status_code}, Actual Status Code: {self.status_code}," \
                                                              f"URL: {self.url}, Response JSON: {self.rs_json}"

    def post(self, endpoint, payload=None, headers=None, expected_status_code=201):
        if not headers:
            headers = {"Content-Type": "application/json"}
        self.url = self.base_url + endpoint
        rs_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"API POST response: {rs_api.json()}")

        return rs_api.json()

    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        self.url = self.base_url + endpoint
        rs_api = requests.get(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"API GET response: {rs_api.json()}")

        return rs_api.json()

