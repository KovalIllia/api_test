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
        print()
        print()
        print()
        print()




        """Get info about created location"""
        get_resource = "/maps/api/place/get/json"
        get_url = f"{base_url}{get_resource}{key}&place_id={place_id}"
        result_get = requests.get(get_url)
        assert result_get.status_code == 200
        print(result_get.text)
        print()
        print()
        print()
        print()



        """Update info about created location"""
        update_resource = "/maps/api/place/update/json"
        update_url = f"{base_url}{update_resource}{key}"
        json_for_update_created_location = {
            "place_id": place_id,
            "address": "70 Summer walk, USA",
            "key": "qaclick123"
        }
        result_update = requests.put(update_url, json=json_for_update_created_location)
        print(result_update.text)
        assert result_update.status_code == 200
        check_put=result_update.json()
        check_put_info=check_put["msg"]
        assert check_put_info=="Address successfully updated"
        print()
        print()
        print()
        print()

        """Get info about updated location"""
        get_resource = "/maps/api/place/get/json"
        get_url = f"{base_url}{get_resource}{key}&place_id={place_id}"
        result_get = requests.get(get_url)
        assert result_get.status_code == 200
        check_adress=result_get.json()
        check_address_info=check_adress["address"]
        assert check_address_info=="70 Summer walk, USA"
        print(result_get.text)
        # print(check_address_info)
        print()
        print()
        print()
        print()

        # """Update info about NOTcreated location -- negative case"""
        # failed_place_id = 555
        # update_resource = "/maps/api/place/update/json"
        # update_url = f"{base_url}{update_resource}{key}"
        # json_for_update_created_location = {
        #     "place_id": failed_place_id,
        #     "address": "70 Summer walk, USA",
        #     "key": "qaclick123"
        # }
        # result_update = requests.put(update_url, json=json_for_update_created_location)
        # print(result_update.text)
        # assert result_update.status_code == 404
        # check_put = result_update.json()
        # check_put_info = check_put["msg"]
        # print(check_put_info)
        # assert check_put_info == "Update address operation failed, looks like the data doesn't exists"
        # print()
        # print()
        # print()


        # """Get info about NOTcreated location  -- negative case"""
        failed_place_id=555
        # get_resource = "/maps/api/place/get/json"
        # get_url = f"{base_url}{get_resource}{key}&place_id={failed_place_id}"
        # result_get = requests.get(get_url)
        # assert result_get.status_code == 404
        # print(result_get.text)
        # print("*****************************")


new_place = TestNewLocation()
new_place.testCreateNewLocation()
