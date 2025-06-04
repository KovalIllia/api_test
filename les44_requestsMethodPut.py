import requests


class TestNewLocation():
    """Working with new location"""

    def testCreateNewLocation(self):
        """Creating  new location"""
        base_url = "https://rahulshettyacademy.com"  # base url
        key = "?key=qaclick123"  # params for requests
        post_resource = "/maps/api/place/get/json"  # resource method POST

        post_url = base_url + post_resource + key
        print(post_url)
        json_for_creation_new_location = {
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
        # result_post=requests.post(post_url)


new_place=TestNewLocation()
new_place.testCreateNewLocation()