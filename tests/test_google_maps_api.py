# from utils.api import *  # або конкретні функції
# from utils.http_methods import *
from requests import Response

from utils.api import Google_maps_api


"""Create, update and delete new place"""
class Test_creat_new_place():

    def test_create_new_place(self):
        print("Method POST")
        result_post: Response = Google_maps_api.create_new_place()

