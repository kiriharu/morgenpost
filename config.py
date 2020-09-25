class Config:
    def __init__(self, telegram_api_token, ids_telegram_users,
                 qiwi_token, qiwi_cross_rates, weatherstack_api_key,
                 weatherstack_locations, rss_max_entries, rss_feeds):
        # Бот токен от телеги вида 71231246:WUGvG2D412415ssFasf3YT6HTTs1
        self.TELEGRAM_API_TOKEN = telegram_api_token
        # ID или юзернеймы (но лучше ID) пользователей телеги, которым посылается сводка
        self.TELEGRAM_USERS_ID = ids_telegram_users

        # Киви токен, получаем тут: https://qiwi.com/api
        self.QIWI_TOKEN = qiwi_token
        # Инфа об обмене валют, вида (откуда, в какую) [("643", "978"), ("643", "840")]
        self.QIWI_CROSS_RATES = qiwi_cross_rates

        # https://weatherstack.com 1000 вызовов в месяц, шикарно, нам хватит.
        self.WEATHERSTACK_API_KEY = weatherstack_api_key
        # имена локаций через запятую, на англицком
        self.WEATHERSTACK_LOCATIONS = weatherstack_locations

        # Количество записей на каждую RSS ленту
        self.RSS_MAX_ENTRIES = rss_max_entries
        # RSS ленты вида (название, линк) [
        #             ("Новости с Яндекса", "https://news.yandex.ru/world.rss"),
        #             ("Новости с Opennet", "https://www.opennet.ru/opennews/opennews_all_utf.rss"),
        #         ]
        self.RSS_FEEDS = rss_feeds


config = Config("",
                ["123456"],
                "",
                [("643", "978"), ("643", "840")],
                "",
                ["Moscow"],
                5,
                [("Новости с Яндекса", "https://news.yandex.ru/world.rss"),
                 ("Новости с Opennet", "https://www.opennet.ru/opennews/opennews_all_utf.rss")]
                )
