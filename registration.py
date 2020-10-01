import typing

from api.interfaces import IApi
from api.telegram import Telegram


class Registration:
    def __init__(self, starting_message: str, *args):
        self.net: typing.Union[Telegram]
        self.chat_ids: typing.List[typing.Union[str, int]]
        self.message = starting_message
        self.work_api: typing.List[typing.Tuple[..., typing.List[...]]] = []

        for api in args:
            is_work = True
            for config in api[1]:
                if not config:
                    is_work = False

            if is_work:
                self.work_api.append((api[0], api[1]))

    def init_telegram(self, token: str, chat_ids: typing.List[typing.Union[str, int]]):
        self.net = Telegram(token)
        self.chat_ids = chat_ids

        return self

    def init_apis(self):
        for APIs_tuple in self.work_api:
            self.message += (APIs_tuple[0])(*APIs_tuple[1]).get()

        return self

    def send(self):
        for chat_id in self.chat_ids:
            self.net.send(self.message, chat_id)
