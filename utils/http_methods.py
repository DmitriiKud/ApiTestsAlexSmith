import allure
import requests

from utils.logger import Logger


class HttpMethods:
    """Список HTTP методов"""
    headers = {'Content-Type': 'application/json'} # Заголовки нашего проекта
    cookie = '' # Куки нашего проекта

    @classmethod
    def get(cls, url):
        with allure.step("GET"):
            Logger.add_request(url=url, method="GET")
            result = requests.get(url=url, headers=cls.headers, cookies=cls.cookie)
            Logger.add_response(result=result)
            return result


    @classmethod
    def post(cls, url, body):
        with allure.step("POST"):
            Logger.add_request(url=url, method="POST")
            result = requests.post(url=url, headers=cls.headers, cookies=cls.cookie, json=body)
            Logger.add_response(result=result)
            return result

    @classmethod
    def put(cls, url, body):
        with allure.step("PUT"):
            Logger.add_request(url=url, method="PUT")
            result = requests.put(url=url, headers=cls.headers, cookies=cls.cookie, json=body)
            Logger.add_response(result=result)
            return result

    @classmethod
    def delete(cls, url, body):
        with allure.step("DELETE"):
            Logger.add_request(url=url, method="DELETE")
            result = requests.delete(url=url, headers=cls.headers, cookies=cls.cookie, json=body)
            Logger.add_response(result=result)
            return result
