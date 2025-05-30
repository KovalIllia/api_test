import requests
import json



""""✅ Задача 1: Перевірка структури відповіді
Мета: Навчитися перевіряти наявність ключових полів у JSON-відповіді.

📌 Умова:
Зроби запит до https://api.chucknorris.io/jokes/random.

🧪 Тести:

Перевір, що статус код дорівнює 200.

Перевір, що у відповіді є ключі: "id", "value", "url" та "created_at".

Перевір, що "value" — це непорожній рядок."""

url="https://api.chucknorris.io/jokes/random"
result=requests.get(url)
assert result.status_code==200
data=result.json()
print(json.dumps(data, indent=2))#Це дозволяє побачити JSON у зручному форматі.
assert "value" in data
assert "id" in data
assert "url" in data
assert "created_at" in data
assert data["value"] is not None#alternative way



"""✅ Задача 2: Отримання жарту з категорії
Мета: Навчитись динамічно підставляти параметри в URL і тестувати специфічні відповіді.

📌 Умова:
Зроби запит до https://api.chucknorris.io/jokes/random?category=dev.

🧪 Тести:

Перевір, що статус код дорівнює 200.

Перевір, що у полі "categories" є елемент "dev".

Перевір, що "value" містить хоча б 10 символів.

💡 Підказка: список усіх категорій можна отримати з https://api.chucknorris.io/jokes/categories."""





"""✅ Задача 3: Пошук жартів за ключовим словом
Мета: Попрактикуватися в роботі з параметрами та кількома результатами.

📌 Умова:
Зроби запит до https://api.chucknorris.io/jokes/search?query=car.

🧪 Тести:

Перевір, що статус код дорівнює 200.

Перевір, що у відповіді ключ "total" > 0.

Перевір, що в масиві "result" хоча б один жарт містить слово "car"."""