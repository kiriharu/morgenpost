from dataclasses import dataclass
import requests
from decimal import Decimal


@dataclass
class BtcRatesInfo:
    rate: Decimal

    def __str__(self) -> str:
        return f"💰 За 1BTC дают {self.rate}USD\n"


class BtcRates:
    def __init__(self):
        self.url: str = f"https://api.bitaps.com/market/v1/ticker/btcusd"

    def get_btc_rates(self) -> str:
        result = Decimal(str((requests.get(self.url).json())["data"]["last"]))
        return str(BtcRatesInfo(
            rate=result
        ))
