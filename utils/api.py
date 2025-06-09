import requests


from utils.http_methods import Http_methods
from tests.test_google_maps_api import *

base_url = "https://rahulshettyacademy.com"  # base url
key = "?key=qaclick123"

"""Methods for testing Google maps api"""


class Google_maps_api():


    """Creating  new location"""
    @staticmethod
    def create_new_place():
        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = "/maps/api/place/add/json"  # resource method POST
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = Http_methods.post(post_url,json_for_create_new_location)
        # place_id=result_post["place_id"]
        print(result_post.text)
        return result_post

    """Get information about created location"""

    @staticmethod
    def get_new_place(place_id):
        get_resource = "/maps/api/place/get/json"  # resource method POST
        get_url = f"{base_url}{get_resource}{key}&place_id={place_id}"
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get


    """Update information about created location"""

    @staticmethod
    def update_new_place(place_id):
        update_resource = "/maps/api/place/update/json"  # resource method PUT
        put_url = f"{base_url}{update_resource}{key}"
        json_for_update_created_location = {
            "place_id": place_id,
            "address": "70 Summer walk, USA",
            "key": "qaclick123"
        }
        result_put = Http_methods.put(put_url,json_for_update_created_location)
        print(result_put.text)
        assert result_put.status_code == 200
        return result_put