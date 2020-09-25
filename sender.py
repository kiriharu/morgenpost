from api import weatherstack, qiwi, telegram, rss
from config import config, Config


class Sender:
    def __init__(self, config_sender: Config, starting_message: str = "Доброе утро! Вот тебе сводка данных с утра: \n\n"):
        self.message_to_send = starting_message
        self.config = config_sender

    def add_text_to_string(self):

        if self.config.WEATHERSTACK_API_KEY:
            self.message_to_send += "☀️Погода сейчас: \n\n"
            weather_api = weatherstack.WeatherStack(self.config.WEATHERSTACK_API_KEY)
            for location in self.config.WEATHERSTACK_LOCATIONS:
                self.message_to_send += weather_api.get_basic_info(location)
            self.message_to_send += "\n"

        if self.config.QIWI_TOKEN:
            self.message_to_send += "🥝Курс в обменнике Qiwi: \n\n"
            qiwi_api = qiwi.Qiwi(self.config.QIWI_TOKEN)
            for crossrate in self.config.QIWI_CROSS_RATES:
                self.message_to_send += qiwi_api.get_cross_rate(*crossrate)
            self.message_to_send += "\n"

        if self.config.RSS_MAX_ENTRIES > 0 and len(self.config.RSS_FEEDS) > 0:
            for feed_params in self.config.RSS_FEEDS:
                feed = rss.RSS(*feed_params)
                entries = feed.parse_feed()
                self.message_to_send += f"🗞 {feed.name}\n"
                for entry in entries:
                    self.message_to_send += f"📍 {str(entry)}\n"
                self.message_to_send += "\n"

    def send_message(self):

        if self.config.TELEGRAM_API_TOKEN:
            tg = telegram.Telegram(self.config.TELEGRAM_API_TOKEN)
            for telegram_user in self.config.TELEGRAM_USERS_ID:
                tg.send(telegram_user, self.message_to_send)


sender = Sender(config_sender=config)
sender.add_text_to_string()
sender.send_message()
