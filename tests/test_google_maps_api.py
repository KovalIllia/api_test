from utils.api import *  # або конкретні функції
from utils.http_methods import *

from utils.api import Google_maps_api

"""Create, update and delete new place"""


class Test_creat_new_place():

    def test_create_new_place(self):
        print("Method POST")
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post["place_id"]

        print("Method GET POST")
        result_get = Google_maps_api.get_new_place(place_id)

        print("Method PUT")
        result_put=Google_maps_api.update_new_place(place_id)

        print("Method GET PUT")
        result_get = Google_maps_api.get_new_place(place_id)

        print("Method DELETE")
        result_get = Google_maps_api.delete_new_place(place_id)

        print("Method GET DELETE")
        result_get = Google_maps_api.get_new_place(place_id)