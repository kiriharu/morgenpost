import requests
from typing import Union, List
from random import randint

class Vkontakte:
    api_url = "https://api.vk.com/method/"

    def __init__(self, token: str):
        self.token = token

    def call(self, method: str, params: dict) -> dict:
        url = f"{self.api_url}{method}"
        return requests.get(url, params).json()

    def send_message(self, user_id: Union[str, int], text: str) -> dict:
        return self.call("messages.send", params=dict(
            user_id=user_id,
            message=text,
            random_id=randint(int(-2e9),
                              int(2e9)),
            access_token=self.token,
            v=999
        ))

    def send(self, text: str, chat_id: Union[str, int]) -> None:
        self.send_message(chat_id, text)
