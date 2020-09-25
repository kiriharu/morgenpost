from config import *
from api import weatherstack, qiwi, telegram, rss
message_to_send = ""
message_to_send += STARTING_MESSAGE

if WEATHERSTACK_API_KEY:
    message_to_send += "☀️Погода сейчас: \n\n"
    weather_api = weatherstack.WeatherStack(WEATHERSTACK_API_KEY)
    for location in WEATHERSTACK_LOCATIONS:
        message_to_send += weather_api.get_basic_info(location)
    message_to_send += "\n"

if QIWI_TOKEN:
    message_to_send += "🥝Курс в обменнике Qiwi: \n\n"
    qiwi_api = qiwi.Qiwi(QIWI_TOKEN)
    for crossrate in QIWI_CROSS_RATES:
        message_to_send += qiwi_api.get_cross_rate(*crossrate)
    message_to_send += "\n"

if RSS_MAX_ENTRIES > 0 and len(RSS_FEEDS) > 0:
    for feed_params in RSS_FEEDS:
        feed = rss.RSS(*feed_params)
        entries = feed.parse_feed()
        message_to_send += f"🗞 {feed.name}\n"
        for entry in entries:
            message_to_send += f"📍 {str(entry)}\n"
        message_to_send += "\n"


if TELEGRAM_API_TOKEN:
    tg = telegram.Telegram(TELEGRAM_API_TOKEN)
    for telegram_user in TELEGRAM_USERS_ID:
        tg.send(telegram_user, message_to_send)


