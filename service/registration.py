import typing
from enum import Enum

from api.social_nets.telegram import Telegram as Tg
from api.social_nets.vkontakte import Vkontakte as Vk

ApiType = typing.TypeVar("ApiType")


class SocialNetType(Enum):
    Telegram = Tg
    Vkontakte = Vk


class ApisList:
    def __init__(self, apis: typing.Optional[typing.List[ApiType]] = None):
        if apis is None:
            self.work_api = []
        else:
            self.work_api: typing.List[ApiType] = apis

    def add_api(self, api: ApiType):
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
