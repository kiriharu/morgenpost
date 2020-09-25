import requests
from typing import Union


class Telegram:
    api_url = "https://api.telegram.org"

    def __init__(self, token: str):
        self.token = token

    def call(self, method: str, params: dict) -> dict:
        url = f"{self.api_url}/bot{self.token}/{method}"
        return requests.get(url, params).json()

    def send_message(self, chat_id: Union[str, int], text: str) -> None:
        self.call("sendMessage", params=dict(
            chat_id=chat_id, text=text
        ))
