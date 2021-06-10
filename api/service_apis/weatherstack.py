from abc import ABC
from typing import List

import requests
from dataclasses import dataclass

from service.interfaces import IApi

@dataclass
class WeatherBasicInfo:
    temperature: int
    feelslike: int
    humidity: int
    pressure: int
    wind_speed: int
    name: str
    weather_descriptions: str

    def __str__(self) -> str:
        return f"{self.name} : {self.weather_descriptions}\n" \
               f"🌡{self.temperature}°C, ощущается как {self.feelslike}°C\n" \
               f"💨{self.wind_speed}, 💧{self.humidity}%, ⬇️ {self.pressure}\n"


class WeatherStack(IApi, ABC):
    url = "http://api.weatherstack.com/current"

    def __init__(self, access_key: str, locations: List[str]):
        self.header = "☀️Погода сейчас: \n\n"
        self.locations = locations
        self.access_key = access_key

    def call(self, params: dict) -> dict:
        params["access_key"] = self.access_key
        result = requests.get(self.url, params).json()
        # оно тут возвращает success: False, если ошибки.
        if not result.get("success", True):
            if result["error"]["code"] == 604:
                raise Exception("Bulk not supported")
            if result["error"]["code"] == 101:
                raise Exception("Invalid access key")
            if result["error"]["code"] == 105:
                raise Exception("Access Restricted")
            raise Exception(result["error"])
        return result

    def get(self) -> str:
        message = self.header

        for location in self.locations:
            query = dict(query=location)
            response = self.call(query)
            message += str(WeatherBasicInfo(
                temperature=response['current']['temperature'],
                feelslike=response['current']['feelslike'],
                humidity=response['current']['humidity'],
                pressure=response['current']['pressure'],
                wind_speed=response['current']['wind_speed'],
                name=response['request']['query'],
                weather_descriptions="".join(response['current']['weather_descriptions'])
            ))

        message += "\n"
        return message
