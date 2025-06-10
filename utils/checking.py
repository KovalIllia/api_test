"""METHODS for checking responses of our requests"""
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
