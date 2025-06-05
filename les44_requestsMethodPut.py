import requests


class TestNewLocation():
    """Working with new location"""

    def testCreateNewLocation(self):
        """Creating  new location"""
        base_url = "https://rahulshettyacademy.com"  # base url
        key = "?key=qaclick123"  # params for requests
        post_resource = "/maps/api/place/add/json"  # resource method POST

        post_url = base_url + post_resource + key
        print(post_url)
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
        result_post = requests.post(post_url, json=json_for_create_new_location)
        assert result_post.status_code == 200
        print(result_post.text)
        check_post = result_post.json()
        # check_info_post = check_post.get("status")
        check_info_post = check_post["status"]
        assert check_info_post == "OK"
        print(f"status:{check_info_post}")
        place_id = check_post["place_id"]
        print(f"place_id:{place_id}")



        """Get info about created location"""

        get_resorce="/maps/api/place/get/json"
        get_url=f"{base_url}{get_resorce}{key}&place_id={place_id}"
        result_get=requests.get(get_url)
        assert result_get.status_code==200
        print(result_get.text)




new_place = TestNewLocation()
new_place.testCreateNewLocation()
