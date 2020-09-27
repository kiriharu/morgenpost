from dataclasses import dataclass
from typing import List
import requests
from decimal import Decimal, ROUND_HALF_UP


@dataclass
class BlockchainRatesInfo:
    symbol: str
    price: Decimal

    def __str__(self) -> str:
        return f"💰 За 1{self.symbol} дают {self.price}USD\n"


class BlockchainRates:
    def __init__(self, symbols: List[str]):
        self.symbols = symbols
        self.url: str = f"http://api.coincap.io/v2/assets"

    def get_blockchain_rates(self) -> str:
        result = (requests.get(self.url).json())["data"]
        message = ""
        for currency in result:
            if currency["symbol"] in self.symbols:
                price = Decimal(currency["priceUsd"])
                price = price.quantize(Decimal("1.0000"), ROUND_HALF_UP)
                message += str(BlockchainRatesInfo(
                    symbol=currency["symbol"],
                    price=price
                ))
        return message
