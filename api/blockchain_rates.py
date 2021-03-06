from abc import ABC
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from typing import List
import requests

from .interfaces import IApi


@dataclass
class BlockchainRatesInfo:
    symbol: str
    price: Decimal

    def __str__(self) -> str:
        return f"💰 За 1{self.symbol} дают {self.price}USD\n"


class BlockchainRates(IApi, ABC):
    def __init__(self, symbols: List[str]):
        self.header = "🏦Курс криптовалют: \n\n"
        self.symbols = symbols
        self.url: str = f"http://api.coincap.io/v2/assets"

    def get(self) -> str:
        result = (requests.get(self.url).json())["data"]
        message = self.header
        for currency in result:
            if currency["symbol"] in self.symbols:
                price = Decimal(currency["priceUsd"])
                price = price.quantize(Decimal("1.0000"), ROUND_HALF_UP)
                message += str(BlockchainRatesInfo(
                    symbol=currency["symbol"],
                    price=price
                ))
        message += "\n"
        return message
