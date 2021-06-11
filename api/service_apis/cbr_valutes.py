from abc import ABC
from typing import List
import requests
from dataclasses import dataclass
from decimal import Decimal

from api.service_apis.interfaces import IApi


class CBRConfig:
    def __init__(self, cross_rates: List[str]):
        self.cross_rates = cross_rates


@dataclass
class CbrValutesInfo:
    valute: str
    nominal: int
    value: Decimal

    def __str__(self):
        return f"💰 За {self.nominal}{self.valute} дают {self.value}RUB\n"


class CbrValutes(IApi, ABC):
    def __init__(self, config: CBRConfig):
        self.header = "🏦Курс валют ЦБР: \n\n"
        self.valutes: List[str] = config.cross_rates
        self.url = "https://www.cbr-xml-daily.ru/daily_json.js"

    def get(self) -> str:
        result = (requests.get(self.url).json())["Valute"]
        message = self.header

        for valute in self.valutes:
            if valute in result:

                message += str(CbrValutesInfo(
                    valute=valute,
                    nominal=result[valute]["Nominal"],
                    value=Decimal(str(result[valute]["Value"]))
                ))

        message += "\n"
        return message
