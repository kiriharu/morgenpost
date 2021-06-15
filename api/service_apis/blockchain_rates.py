from abc import ABC
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from typing import List
import requests

from api.service_apis.interfaces import IApi


class BlockchainConfig:
    def __init__(self, blockchain_rates: List[str]):
        self.blockchain_rates = blockchain_rates


@dataclass
class BlockchainRatesInfo:
    symbol: str
    price: Decimal

    def __str__(self) -> str:
        return f"💰 За 1{self.symbol} дают {self.price}USD\n"


class BlockchainRates(IApi):
    def __init__(self, config: BlockchainConfig):
        self.symbols = config.blockchain_rates

    @property
    def url(self):
        return "http://api.coincap.io/v2/assets"

    @property
    def header(self):
        return "🏦Курс криптовалют: \n\n"

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
