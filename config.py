import os
import json

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
TELEGRAM_USERS_ID = json.loads(os.getenv("TELEGRAM_USERS_ID", "[]"))

# Юзер токен от ВК
VK_API_TOKEN = os.getenv("VK_API_TOKEN")
# ID пользователей ВК, которым посылается сводка
VK_USERS_ID = json.loads(os.getenv("VK_USERS_ID", "[]"))

# Стартовое сообщение
STARTING_MESSAGE = "Доброе утро! Вот тебе сводка данных с утра: \n\n"

# Киви токен, получаем тут: https://qiwi.com/api
QIWI_TOKEN = os.getenv("QIWI_TOKEN")
# Инфа об обмене валют, вида (откуда, в какую)
QIWI_CROSS_RATES = json.loads(os.getenv("QIWI_CROSS_RATES"))
print(QIWI_CROSS_RATES)
# QIWI_CROSS_RATES = [("643", "978"), ("643", "840")] deprecated

# Информация об обмене валют в массиве.
# Будет дано сколько рублей стоит определенное количество единиц валюты, выданное РБК.
CBR_CROSS_RATES = json.loads(os.getenv("CBR_CROSS_RATES"))
# CBR_CROSS_RATES = ["USD", "EUR", "ZAR"] deprecated

# Курс каких криптовалют получать
# Обозначения валют на английском
BLOCKCHAIN_RATES = json.loads(os.getenv("BLOCKCHAIN_RATES"))
# BLOCKCHAIN_RATES = ["BTC", "USDT", "XEM"] deprecated

# https://weatherstack.com 1000 вызовов в месяц, шикарно, нам хватит.
WEATHERSTACK_API_KEY = os.getenv("WEATHERSTACK_API_KEY")
# имена локаций через запятую, на английском
WEATHERSTACK_LOCATIONS = json.loads(os.getenv("WEATHERSTACK_LOCATIONS"))
# WEATHERSTACK_LOCATIONS = ["Moscow", "Minsk"] deprecated

# имена локаций, любой Unicode язык
# если пусто: модуль выключается
WTTRIN_LOCATIONS = json.loads(os.getenv("WTTRIN_LOCATIONS"))
# WTTRIN_LOCATIONS = ["Москва", "Берлин"] deprecated

# COVID19 информация по странам
# Названия стран брать из https://coronavirus-19-api.herokuapp.com/ -> Countries
COVID_COUNTRIES = json.loads(os.getenv("COVID_COUNTRIES"))
# COVID_COUNTRIES = ["Russia", "India", "Brazil"] deprecated
# Режим работы: расширенный "EXTENDED" или краткий "SHORT"
# По умолчанию: EXTENDED
COVID_MODE = os.getenv("COVID_MODE")
# COVID_MODE = "SHORT" deprecated

# Количество записей на каждую RSS ленту
RSS_MAX_ENTRIES = os.getenv("RSS_MAX_ENTRIES")
try:
    RSS_MAX_ENTRIES = int(RSS_MAX_ENTRIES)
except ValueError:
    raise ValueError("RSS_MAX_ENTRIES can only be an integer, not a string")
# RSS_MAX_ENTRIES = 5 deprecated
# RSS ленты вида (название, линк)
RSS_FEEDS = json.loads(os.getenv("RSS_FEEDS"))
# RSS_FEEDS = [
#     ["Новости с Яндекса", "https://news.yandex.ru/world.rss"],
#     ["Новости с Opennet", "https://www.opennet.ru/opennews/opennews_all_utf.rss"],
# ] deprecated

if WEATHERSTACK_API_KEY and WEATHERSTACK_LOCATIONS:
    weatherstack_config = WeatherStackConfig(token=WEATHERSTACK_API_KEY, locations=WEATHERSTACK_LOCATIONS)
else:
    weatherstack_config = None

if WTTRIN_LOCATIONS:
    wttrin_config = WttrInConfig(locations=WTTRIN_LOCATIONS)
else:
    wttrin_config = None

if QIWI_TOKEN and QIWI_CROSS_RATES:
    qiwi_config = QiwiConfig(token=QIWI_TOKEN, cross_rates=QIWI_CROSS_RATES)
else:
    qiwi_config = None

if CBR_CROSS_RATES:
    cbr_config = CBRConfig(CBR_CROSS_RATES)
else:
    cbr_config = None

if BLOCKCHAIN_RATES:
    blockchain_config = BlockchainConfig(BLOCKCHAIN_RATES)
else:
    blockchain_config = None

if COVID_COUNTRIES and COVID_MODE:
    covid19_config = Covid19Config(countries=COVID_COUNTRIES, mode=COVID_MODE)
else:
    covid19_config = None

if RSS_FEEDS and RSS_MAX_ENTRIES:
    rss_config = RSSConfig(max_entries=RSS_MAX_ENTRIES, feeds=RSS_FEEDS)
else:
    rss_config = None
