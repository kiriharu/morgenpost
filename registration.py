import typing
from enum import Enum

from api.telegram import Telegram
from api.vkontakte import Vkontakte

T = typing.TypeVar("T")

class GlobalApi:
    def __init__(self, api: T, configs: typing.List[T]):
        self.api = api
        self.configs = configs

    def setup_and_get(self):
        try:
            ready_api = self.api(*self.configs)
        except Exception:
            raise ValueError(f"Cannot initialize {type(self.api).__name__}")

        return ready_api

class Registration:
    def __init__(self, starting_message: str, type_net, apis: typing.List[GlobalApi]):
        self.type_net: str = type_net.lower()
        self.type_net: Registration.NetType
        self.net: T = None
        self.chat_ids: typing.List[typing.Union[str, int]] = []
        self.message = starting_message
        self.work_api: typing.List[GlobalApi] = apis

    def init_net(self, token: str, chat_ids: typing.List[typing.Union[str, int]]):
        if self.type_net == Registration.NetType.Telegram:
            self.net = Telegram(token)
            self.chat_ids = chat_ids

        elif self.type_net == Registration.NetType.VK:
            self.net = Vkontakte(token)
            self.chat_ids = chat_ids

        elif self.type_net == Registration.NetType.Discord:
            pass

        return self

    def init_apis(self):
        for api in self.work_api:
            self.message += api.setup_and_get().get()

        return self

    def send(self):
        for chat_id in self.chat_ids:
            self.net.send(self.message, chat_id)

    class NetType(Enum):
        Telegram = 0
        VK = 1
        Discord = 2

