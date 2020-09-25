from dataclasses import dataclass
import requests


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

    def __str__(self):
        return f"🏙 {self.city}, " \
               f"{self.weather.lower()}\n" \
               f"🌡{self.temperature}°C, ощущается как {self.feels_like_C}°C, " \
               f"💧{self.humidity}%, " \
               f"🔮{self.uv_index}\n" \
               f"💨{self.wind_speed}km/h, " \
               f"👁{self.visibility}/10, " \
               f"☁{self.cloudcover}\n"


class WttrIn:
    def __init__(self, city):
        self.city: str = city
        self.url: str = f"https://wttr.in/{city}?0&format=j1&lang=ru&m&M"

    def get_basic_info(self):
        result = ((requests.get(self.url).json())['current_condition'])[0]
        return str(WttrInInfo(
            city=self.city,
            temperature=result['temp_C'],
            feels_like_C=result['FeelsLikeC'],
            cloudcover=result['cloudcover'],
            humidity=result['humidity'],
            weather=result['lang_ru'][0]['value'],
            uv_index=result['uvIndex'],
            visibility=result['visibility'],
            wind_speed=result['windspeedKmph']
        ))
