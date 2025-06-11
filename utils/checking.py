"""METHODS for checking responses of our requests"""
import json

import requests
from requests import Response


class Checking():
    """method for checking status code"""

    @staticmethod
    def check_status_code(response: requests.Response, status_code):
        assert status_code == response.status_code  # espectedResult==actualResult
        if response.status_code == status_code:
            print(f"success! status code: {response.status_code}")
        else:
            print(f"failed! status code: {response.status_code}")




    """method for checking for required fields in a query response"""
    @staticmethod
    def check_json_token(response: requests.Response, expected_value):
        token=json.loads(response.text)#форматує string в формат json
        assert list(token)==expected_value
        print("all required field are presented")