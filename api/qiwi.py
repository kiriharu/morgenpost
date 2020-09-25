import requests
from dataclasses import dataclass


def replace_by_name(code):
    if code == "643":
        return "RUB"
    if code == "978":
        return "EUR"
    if code == "840":
        return "USD"


@dataclass
class CrossRate:
    from_e: str
    to: str
    rate: float

    def __str__(self) -> str:
        return f"💰 За 1 {replace_by_name(self.to)} дают {replace_by_name(self.from_e)} {self.rate}\n"


class Qiwi:
    url = "https://edge.qiwi.com"

    def __init__(self, api_token: str):
        self.session = requests.Session()
        self.session.headers = {
            "authorization": f"Bearer {api_token}",
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

    def get_cross_rate(self, rate_from: str, rate_to: str) -> str:
        crossrate_dict = [x for x in self.cross_rates()
                      if x['from'] == rate_from and x['to'] == rate_to][0]
        return str(CrossRate(
            from_e=crossrate_dict['from'],
            to=crossrate_dict['to'],
            rate=crossrate_dict['rate']
        ))
