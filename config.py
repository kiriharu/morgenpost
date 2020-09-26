# Бот токен от телеги вида 71231246:WUGvG2D412415ssFasf3YT6HTTs1
TELEGRAM_API_TOKEN = ""
# ID или юзернеймы (но лучше ID) пользователей телеги, которым посылается сводка
TELEGRAM_USERS_ID = [1234567]

# Стартовое сообщение
STARTING_MESSAGE = "Доброе утро! Вот тебе сводка данных с утра: \n\n"

# Киви токен, получаем тут: https://qiwi.com/api
QIWI_TOKEN = ""
# Инфа об обмене валют, вида (откуда, в какую)
QIWI_CROSS_RATES = [("643", "978"), ("643", "840")]

# Информация об обмене валют в массиве.
# Будет дано сколько рублей стоит определенное количество единиц валюты, выданное РБК.
RBC_CROSS_RATES = ["USD", "EUR", "ZAR"]

# Нужно ли получать курс BTC (долларов за единицу)
IS_NEED_BTC = True

# https://weatherstack.com 1000 вызовов в месяц, шикарно, нам хватит.
WEATHERSTACK_API_KEY = ""
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