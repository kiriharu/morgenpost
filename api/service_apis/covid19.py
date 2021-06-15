from abc import ABC
from typing import List
import requests
from dataclasses import dataclass

from api.service_apis.interfaces import IApi


class Covid19Config:
    def __init__(self, countries: List[str], mode: str):
        self.countries = countries
        self.mode = mode


@dataclass
class Covid19Info:
    mode: str
    country: str
    cases: int
    today_cases: int
    deaths: int
    active: int
    today_deaths: int = None
    recovered: int = None
    critical: int = None

    def __str__(self) -> str:
        if self.mode == "EXTENDED":
            return f"🦠Страна: {self.country}\n" \
                   f"Всего: {self.cases}\n" \
                   f"➕Болеют всего: {self.active}; сегодня: {self.today_cases}\n" \
                   f"⚰️Умерших всего: {self.deaths}; сегодня: {self.today_deaths}\n" \
                   f"🤒В крит. состоянии: {self.critical}\n" \
                   f"😷Выздоровевших: {self.recovered}\n\n"
        elif self.mode == "SHORT":
            return f"🦠{self.country}:\n" \
                   f"⚰️{self.deaths}, ➕{self.today_cases}, 🤒{self.active}\n" \
                   f"😷{self.cases}\n\n"


class Covid19(IApi):

    def __init__(self, config: Covid19Config):
        self.countries = config.countries

        if (config.mode == "") or (config.mode != "SHORT" and config.mode != "EXTENDED"):
            self.mode = "EXTENDED"
        else:
            self.mode = config.mode

    @property
    def url(self):
        return "https://coronavirus-19-api.herokuapp.com/countries/"

    @property
    def header(self):
        return "🦠Статистика по коронавирусу: \n\n"

    def get(self) -> str:
        message = ""
        for country in self.countries:
            url = self.url + country
            result = requests.get(url)
            if result.content != b'Country not found':
                result = result.json()
                if self.mode == "EXTENDED":
                    message += str(Covid19Info(
                        mode=self.mode,
                        country=country,
                        cases=result["cases"],
                        today_cases=result["todayCases"],
                        active=result["active"],
                        deaths=result["deaths"],
                        today_deaths=result["todayDeaths"],
                        recovered=result["recovered"],
                        critical=result["critical"]
                    ))
                elif self.mode == "SHORT":
                    message += str(Covid19Info(
                        mode=self.mode,
                        country=country,
                        cases=result["cases"],
                        today_cases=result["todayCases"],
                        active=result["active"],
                        deaths=result["deaths"],
                    ))

        if message == "":
            message = "Статистика отсутствует, проверьте данные в массиве!"

        message += "\n"
        return message
