import os
import json
import typing

from dotenv import load_dotenv

from api.service_apis.blockchain_rates import BlockchainConfig
from api.service_apis.cbr_valutes import CBRConfig
from api.service_apis.covid19 import Covid19Config
from api.service_apis.qiwi import QiwiConfig
from api.service_apis.rss import RSSConfig
from api.service_apis.weatherstack import WeatherStackConfig
from api.service_apis.wttr_in import WttrInConfig

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Бот токен от телеги вида 71231246:WUGvG2D412415ssFasf3YT6HTTs1
TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
# ID или юзернеймы (но лучше ID) пользователей телеги, которым посылается сводка
TELEGRAM_USERS_ID = json.loads(os.getenv("TELEGRAM_USERS_ID"))

# Стартовое сообщение
STARTING_MESSAGE = "Доброе утро! Вот тебе сводка данных с утра: \n\n"

# Киви токен, получаем тут: https://qiwi.com/api
QIWI_TOKEN = os.getenv("QIWI_TOKEN")
# Инфа об обмене валют, вида (откуда, в какую)
QIWI_CROSS_RATES = [("643", "978"), ("643", "840")]

# Информация об обмене валют в массиве.
# Будет дано сколько рублей стоит определенное количество единиц валюты, выданное РБК.
CBR_CROSS_RATES = ["USD", "EUR", "ZAR"]

# Курс каких криптовалют получать
# Обозначения валют на английском
BLOCKCHAIN_RATES = ["BTC", "USDT", "XEM"]

# https://weatherstack.com 1000 вызовов в месяц, шикарно, нам хватит.
WEATHERSTACK_API_KEY = os.getenv("WEATHERSTACK_API_KEY")
# имена локаций через запятую, на англицком
WEATHERSTACK_LOCATIONS = ["Moscow", "Minsk"]

# имена локаций, любой Unicode язык
# если пусто: модуль выключается
WTTRIN_LOCATIONS = ["Москва", "Берлин"]

# COVID19 информация по странам
# Названия стран брать из https://coronavirus-19-api.herokuapp.com/ -> Countries
COVID_COUNTRIES = ["Russia", "India", "Brazil"]
# Режим работы: расширенный "EXTENDED" или краткий "SHORT"
# По умолчанию: EXTENDED
COVID_MODE = "SHORT"

# Количество записей на каждую RSS ленту
RSS_MAX_ENTRIES = 5
# RSS ленты вида (название, линк)
RSS_FEEDS = [
    ("Новости с Яндекса", "https://news.yandex.ru/world.rss"),
    ("Новости с Opennet", "https://www.opennet.ru/opennews/opennews_all_utf.rss"),
]

weatherstack_config = WeatherStackConfig(token=WEATHERSTACK_API_KEY, locations=WEATHERSTACK_LOCATIONS)
wttrin_config = WttrInConfig(locations=WTTRIN_LOCATIONS)
qiwi_config = QiwiConfig(token=QIWI_TOKEN, cross_rates=QIWI_CROSS_RATES)
cbr_config = CBRConfig(CBR_CROSS_RATES)
blockchain_config = BlockchainConfig(BLOCKCHAIN_RATES)
covid19_config = Covid19Config(countries=COVID_COUNTRIES, mode=COVID_MODE)
rss_config = RSSConfig(max_entries=RSS_MAX_ENTRIES, feeds=RSS_FEEDS)
