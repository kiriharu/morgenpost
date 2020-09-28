from config import *
from api import (
    weatherstack, qiwi, telegram,
    rss, wttr_in, cbr_valutes,
    covid19, blockchain_rates
)

message_to_send = ""
message_to_send += STARTING_MESSAGE

if WEATHERSTACK_API_KEY:
    message_to_send += weatherstack.WeatherStack(WEATHERSTACK_API_KEY, WEATHERSTACK_LOCATIONS).get()

if WTTRIN_LOCATIONS:
    message_to_send += wttr_in.WttrIn(WTTRIN_LOCATIONS).get()

if QIWI_TOKEN:
    message_to_send += qiwi.Qiwi(QIWI_TOKEN, QIWI_CROSS_RATES).get()

if CBR_CROSS_RATES:
    message_to_send += cbr_valutes.CbrValutes(CBR_CROSS_RATES).get()

if BLOCKCHAIN_RATES:
    message_to_send += blockchain_rates.BlockchainRates(BLOCKCHAIN_RATES).get()

if COVID_COUNTRIES:
    if COVID_MODE:
        message_to_send += covid19.Covid19(COVID_COUNTRIES, COVID_MODE).get()
    else:
        message_to_send += covid19.Covid19(COVID_COUNTRIES, "EXTENDED").get()

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
