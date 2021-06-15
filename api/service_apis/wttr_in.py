from abc import ABC
from dataclasses import dataclass
from typing import List

import requests

from api.service_apis.interfaces import IApi


class WttrInConfig:
    def __init__(self, locations: List[str]):
        self.locations = locations


@dataclass
class WttrInInfo:
    city: str
    temperature: str
    feels_like_C: str
    cloudcover: str
    humidity: str
    weather: str
    uv_index: str
    visibility: str
    wind_speed: str

    def __str__(self) -> str:
        return f"🏙 {self.city}, " \
               f"{self.weather.lower()}\n" \
               f"🌡{self.temperature}°C, ощущается как {self.feels_like_C}°C, " \
               f"💧{self.humidity}%, " \
               f"🔮{self.uv_index}\n" \
               f"💨{self.wind_speed}km/h, " \
               f"👁{self.visibility}/10, " \
               f"☁{self.cloudcover}\n"


class WttrIn(IApi):
    def __init__(self, config: WttrInConfig):
        self.cities = config.locations

    @property
    def url(self):
        return "https://wttr.in/"

    @property
    def header(self):
        return "☀️Погода сейчас: \n\n"

    def get(self) -> str:
        message = self.header
        for city in self.cities:
            url = self.url + f"{city}?0&format=j1&lang=ru&m&M"
            result = ((requests.get(url).json())['current_condition'])[0]
            message += str(WttrInInfo(
                city=city,
                temperature=result['temp_C'],
                feels_like_C=result['FeelsLikeC'],
                cloudcover=result['cloudcover'],
                humidity=result['humidity'],
                weather=result['lang_ru'][0]['value'],
                uv_index=result['uvIndex'],
                visibility=result['visibility'],
                wind_speed=result['windspeedKmph']
            ))
        message += "\n"
        return message
