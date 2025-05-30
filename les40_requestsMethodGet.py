import requests


url="https://api.chucknorris.io/jokes/random"
result=requests.get(url)
print(f"status code: {result.status_code}")
assert 200==result.status_code#negative case
if result.status_code==200:
    print(f"Success operation.Get new joke!")
else:
    print(f"Operation failed!")
result.encoding='utf-8'
print(result.text)