from config import *
from api import weatherstack, qiwi, telegram
message_to_send = ""
message_to_send += STARTING_MESSAGE

if WEATHERSTACK_API_KEY:
    message_to_send += "☀️Погода сейчас: \n"
    weather_api = weatherstack.WeatherStack(WEATHERSTACK_API_KEY)
    for location in WEATHERSTACK_LOCATIONS:
        message_to_send += weather_api.get_basic_info(location)

if QIWI_TOKEN:
    message_to_send += "🥝Курс в обменнике Qiwi: \n"
    qiwi_api = qiwi.Qiwi(QIWI_TOKEN)
    for crossrate in QIWI_CROSS_RATES:
        message_to_send += qiwi_api.get_cross_rate(*crossrate)

if TELEGRAM_API_TOKEN:
    tg = telegram.Telegram(TELEGRAM_API_TOKEN)
    for telegram_user in TELEGRAM_USERS_ID:
        tg.send_message(telegram_user, message_to_send)


