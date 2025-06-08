import json

import requests


class TestNewJoke():
    """Creating new joke"""

    def __init__(self):
        pass

    def test_creating_new_random_joke(self):
        """Creating new joke"""
        result = requests.get("https://api.chucknorris.io/jokes/random")
        assert 200 == result.status_code
        print(f"Success operation.Get new joke!")
        assert result.status_code == 200
        data = result.json()
        print(json.dumps(data, indent=2))
        # check_info=data.get("categories")
        # print(check_info)
        # assert check_info==[]
        assert data["categories"] == []  # alternative to code 19-21
        assert "Chuck" in data["value"]

    # """test from 43Lesson"""
    def test_creating_new_random_category_joke(self):
        """Creating new random joke from category"""
        result = requests.get("https://api.chucknorris.io/jokes/random?category=sport")
        assert result.status_code == 200
        data = result.json()
        print(json.dumps(data, indent=2))

    def test_negativeCaseToGetRandomJoke(self):
        result = requests.get("https://api.chucknorris.io/jokes/random?category=spo")
        data = result.json()
        print(json.dumps(data, indent=2))
        assert result.status_code == 404


# random_joke=TestNewJoke()
# random_joke.test_creating_new_random_joke()
# sport_category_joke=TestNewJoke()
# sport_category_joke.test_creating_new_random_category_joke()
spo_NegativeCase = TestNewJoke()
spo_NegativeCase.test_negativeCaseToGetRandomJoke()
