import typing
from enum import Enum

from api.social_nets.telegram import Telegram
from api.social_nets.vkontakte import Vkontakte

T = typing.TypeVar("T")


class SocialNetType(Enum):
    Telegram = 0
    VK = 1
    Discord = 2


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


class ApisList:
    def __init__(self, apis: typing.Optional[typing.List[GlobalApi]] = None):
        if apis is None:
            self.work_api = []
        else:
            self.work_api: typing.List[GlobalApi] = apis

    def init_apis(self):
        for api in self.work_api:
            self.work_api += api.setup_and_get()

        return self

    def add_api(self, api: T, configs: typing.List[T]):
        concrete_api = GlobalApi(api, configs).setup_and_get()
        self.work_api.append(concrete_api)
        return self

    def get_str(self):
        return self.__str__()

    def __str__(self):
        message = ""
        if self.work_api:
            for api in self.work_api:
                message += api.get()
                message += "\n"
        else:
            message += "Новостей на сегодня нет, ибо список сервисов пуст!"

        return message


class SocialNet:
    def __init__(self, type_net: SocialNetType, token: typing.Optional[str] = None):
        self.type_net: SocialNet.NetType = type_net
        if token is not None:
            self.init_net(token)
        else:
            self.net: T = None

    def send(self, message, chat_ids):
        for chat_id in chat_ids:
            self.net.send(message, chat_id)

    def init_net(self, token: str):
        if self.type_net == SocialNetType.Telegram:
            self.net = Telegram(token)

        elif self.type_net == SocialNetType.VK:
            self.net = Vkontakte(token)

        elif self.type_net == SocialNetType.Discord:
            pass

        return self
