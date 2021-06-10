from abc import ABC
from typing import List, Tuple

import requests
from dataclasses import dataclass

from service.interfaces import IApi


def replace_by_name(code):
    if code == "643":
        return "RUB"
    if code == "978":
        return "EUR"
    if code == "840":
        return "USD"


class QiwiConfig:
    def __init__(self, token: str, cross_rates: List[Tuple[str, str]]):
        self.token = token
        self.cross_rates = cross_rates


@dataclass
class CrossRate:
    from_e: str
    to: str
    rate: float

    def __str__(self) -> str:
        return f"💰 За 1 {replace_by_name(self.to)} дают {replace_by_name(self.from_e)} {self.rate}\n"


class Qiwi(IApi, ABC):
    url = "https://edge.qiwi.com"

    def __init__(self, config: QiwiConfig):
        self.header = "🥝Курс в обменнике Qiwi: \n\n"
        self.valutes = config.cross_rates
        self.session = requests.Session()
        self.session.headers = {
            "authorization": f"Bearer {config.token}",
            "content-type": "application/json",
            "Accept": "application/json"
        }

    def call(self, method: str) -> dict:
        result = self.session.get(f"{self.url}{method}")
        if result.status_code == 401:
            raise Exception("Authorization failed")
        return result.json()['result']

    def cross_rates(self):
        return self.call("/sinap/crossRates")

    def get(self) -> str:
        message = self.header
        for rates in self.valutes:
            rate_from, rate_to = rates[0], rates[1]
            crossrate_dict = [x for x in self.cross_rates()
                          if x['from'] == rate_from and x['to'] == rate_to][0]

            message += str(CrossRate(
                from_e=crossrate_dict['from'],
                to=crossrate_dict['to'],
                rate=crossrate_dict['rate']
            ))
        message += "\n"
        return message
