import json
import requests

"""🔹 Задача 1: Створення класу для API-запитів
Ціль: створити клас, що інкапсулює GET-запити до https://api.chucknorris.io.
Умова:
Створи клас ChuckNorrisAPI з методом get_random_joke().
Метод має повертати JSON-відповідь.
Перевір, що статус-код дорівнює 200.
Порада: використай requests.get() всередині методу."""


class ChuckNorrisAPI():
    """створити клас, що інкапсулює GET-запити до https://api.chucknorris.io."""

    def __init__(self):
        self.url="https://api.chucknorris.io"

    def get_random_joke(self):
        category="/jokes/random"
        result = requests.get(self.url+category)
        assert result.status_code == 200
        data = result.json()
        return data

# Задача 2: Запит за категорією через метод.Ціль: розширити попередній клас.
# Умова:Додай метод get_joke_by_category(category).Метод має приймати назву категорії як параметр і повертати жарт.
# Зроби перевірку, що "categories" у відповіді містить цю категорію.
    def get_joke_by_category(self,category = "movie"):
        # category="movie"
        category_path=f"/jokes/random?category={category}"
        result=requests.get(self.url+category_path)
        assert result.status_code == 200
        data=result.json()
        assert category in data["categories"]
        return data

    def alternative_get_joke_by_category(self,category = "movie"):
        # category="movie"
        category_path=f"/jokes/random?category={category}"
        try:
            result=requests.get(self.url+category_path)
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to fetch joke: {e}")
        if result.status_code != 200:
            raise RuntimeError(f"Expected status code 200, but got {result.status_code}")
        try:
            data=result.json()
        except ValueError:
            raise RuntimeError("Response is not valid JSON")
        assert category in data["categories"]
        if category not in data["categories"]:
            raise ValueError(f"Category {category} not found")
        return data


# Задача 3: Отримати список доступних категорій.Ціль: попрактикуватись у роботі з масивами з відповіді.
# Умова:Додай метод get_categories(),який повертає список доступних категорій.
# Перевір, що в списку присутня категорія 'dev'.

    def get_categories(self):
        category="/jokes/categories"
        result=requests.get(self.url+category)
        assert result.status_code==200
        data=result.json()
        assert "dev" in data
        if "dev" not in data:
            raise ValueError(f"Category !'dev'! not found")
        return data


# Задача 4: Пошук жартів за ключовим словом.Ціль: зробити параметризований GET-запит з query.
# Умова:Додай метод search_jokes(query).Метод має повертати список жартів.
# Перевір, що хоча б один жарт містить ключове слово у тексті (value).

    def search_jokes(self,category="science"):
        category_pas=f"/jokes/search?query={category}"
        result=requests.get(self.url+category_pas)
        assert result.status_code==200
        result_data=result.json()
        category_joke=0
        for i in result_data["result"]:
            joke_text_result = i["value"]
            if "science" in joke_text_result:
                category_joke+=1
            # print(category_joke)
        return result_data

# Задача 5: Отримання кількох жартів у циклі.Ціль: закріпити цикл виклику API.
# Умова: Напиши функцію (поза класом), яка 5 разів викликає get_random_joke() і зберігає всі тексти жартів у список.
# Перевір, що всі жартів у списку не порожні (len(joke) > 0).

def get_random_joke():
    newJoke=ChuckNorrisAPI()
    joke_text_result=[]
    for i in range(5):
        get_some_joke = newJoke.get_random_joke()
        data=get_some_joke["value"]
        assert len(data)>0
        joke_text_result.append(data)
    assert len(joke_text_result) > 0
    print(joke_text_result)

    # result=requests.get("https://api.chucknorris.io/jokes/random")
    # assert result.status_code==200
    # data=result.json()





random_joke = ChuckNorrisAPI()
joke_data=random_joke.get_random_joke()
# print(json.dumps(joke_data,indent=2))

random_category_joke=ChuckNorrisAPI()
random_category_joke_data=random_category_joke.get_joke_by_category()
# print(json.dumps(random_category_joke_data,indent=2))

random_category_joke_alternative=ChuckNorrisAPI()
random_category_joke_alternative_data=random_category_joke_alternative.alternative_get_joke_by_category()
# print(json.dumps(random_category_joke_alternative_data,indent=2))

available_list=ChuckNorrisAPI()
available_list_data=available_list.get_categories()
# print(json.dumps(available_list_data,indent=2))

search_jokes_category=ChuckNorrisAPI()
search_jokes_category_data=search_jokes_category.search_jokes()
# print(json.dumps(search_jokes_category_data,indent=2))

get_random_joke()
























