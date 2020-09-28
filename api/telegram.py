import requests
from typing import Union, List


class Telegram:
    api_url = "https://api.telegram.org"

    def __init__(self, token: str, chat_ids: List[Union[str, int]] = None):
        self.chat_ids = chat_ids
        self.token = token

    def call(self, method: str, params: dict) -> dict:
        url = f"{self.api_url}/bot{self.token}/{method}"
        return requests.get(url, params).json()

    def send_message(self, chat_id: Union[str, int], text: str) -> dict:
        self.call("sendMessage", params=dict(
            chat_id=chat_id, text=text, parse_mode="Markdown", disable_web_page_preview=True
        ))

    def send(self, text: str, chat_id: Union[str, int] = None) -> None:
        if chat_id:
            if len(text) > 4096:
                for x in range(0, len(text), 4096):
                    self.send_message(chat_id, text[x:x+4096])
            else:
                self.send_message(chat_id, text)
        else:
            for id_chat in self.chat_ids:
                self.send_message(id_chat, text)
