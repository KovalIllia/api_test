from utils.http_methods import Http_methods

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
        print(result_post.text)
        return result_post