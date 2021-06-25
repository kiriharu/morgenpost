import typing
from enum import Enum

from api.social_nets.telegram import Telegram as Tg
from api.social_nets.vkontakte import Vkontakte as Vk
from service.exceptions import SocialNetworkNotFoundException

T = typing.TypeVar("T")


class SocialNetType(Enum):
    Telegram = Tg
    Vkontakte = Vk


class ApisList:
    def __init__(self, apis: typing.Optional[typing.List[T]] = None):
        if apis is None:
            self.work_api = []
        else:
            self.work_api: typing.List[T] = apis

    def init_apis(self):
        for api in self.work_api:
            self.work_api += api.setup_and_get()

        return self

    def add_api(self, api: T):
        self.work_api.append(api)
        return self

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
        self.type_net: SocialNetType = type_net
        if token is not None:
            self.init_net(token)
        else:
            self.net: T = None

    def send(self, message, chat_ids):
        for chat_id in chat_ids:
            self.net.send(message, chat_id)

    def init_net(self, token: str):
        try:
            self.net = self.type_net.value(token)
        except TypeError:
            raise SocialNetworkNotFoundException("Вы указали несуществующую в программе социальную сеть!")
        return self
