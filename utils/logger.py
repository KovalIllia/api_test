import datetime
import os

import requests


class Logger():

    file_name=f"logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"


    @classmethod
    def wrire_log_to_file(cls,data:str):
        with open(cls.file_name, 'a',encoding='utf=8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls,url:str, method: str):
        test_name=os.environ.get("PYTEST_CURRENT_TEST")#назва тесту який виконується

        data_to_add = f"\n-----\n"#дані які додаються з переносами і пробілами
        data_to_add += f"Test:  {test_name}\n"
        data_to_add += f"Time:  {str(datetime.datetime.now())}\n"
        data_to_add += f"Request method:  {method}\n"
        data_to_add += f"Request URL:  {url}\n"
        data_to_add += "\n"

        cls.wrire_log_to_file(data_to_add)


    @classmethod
    def add_response(cls,result: requests.Response):
        cookie_as_dict=dict(result.cookies)#поміщ в файл
        headers_as_dict=dict(result.headers)#поміщ в файл

        data_to_add = f"Response code: {result.status_code}\n"#які дані ще додаються в файл -- при оголошенні тільки "=", а не "+="
        data_to_add += f"Response text: {result.text}\n"#які дані ще додаються в файл
        data_to_add += f"Response headers: {headers_as_dict}\n"#які дані ще додаються в файл
        data_to_add += f"Response cookies: {cookie_as_dict}\n"#які дані ще додаються в файл
        data_to_add = f"\n-----\n"  # string для розділення

        cls.wrire_log_to_file(data_to_add)

