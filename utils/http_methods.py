import allure
import requests
from utils import *
from utils.logger import Logger

"""List of http methods"""


class Http_methods():
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        with allure.step("GET"):
            Logger.add_request(url,method="GET") #після виклику в логах буде відображатись запис
            result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            Logger.add_request(url, method="POST")  # після виклику в логах буде відображатись запис
            result = requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)
            return result


    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            Logger.add_request(url, method="PUT")  # після виклику в логах буде відображатись запис
            result = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step("DELETE"):
            Logger.add_request(url, method="DELETE")  # після виклику в логах буде відображатись запис
            result = requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)
            return result