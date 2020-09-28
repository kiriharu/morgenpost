from config import *
from api import (
    weatherstack, qiwi, telegram,
    rss, wttr_in, cbr_valutes,
    covid19, blockchain_rates
)
from registration import Registration

Registration(STARTING_MESSAGE,
             (weatherstack.WeatherStack, [WEATHERSTACK_API_KEY, WEATHERSTACK_LOCATIONS]),
             (wttr_in.WttrIn, [WTTRIN_LOCATIONS]),
             (qiwi.Qiwi, [QIWI_TOKEN, QIWI_CROSS_RATES]),
             (cbr_valutes.CbrValutes, [CBR_CROSS_RATES]),
             (blockchain_rates.BlockchainRates, [BLOCKCHAIN_RATES]),
             (covid19.Covid19, [COVID_COUNTRIES, COVID_MODE]),
             (rss.RSS, [RSS_FEEDS, RSS_MAX_ENTRIES]))\
    .init_telegram(TELEGRAM_API_TOKEN, TELEGRAM_USERS_ID)\
    .init_apis()\
    .send()