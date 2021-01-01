from config import (
    STARTING_MESSAGE,
    WEATHERSTACK_API_KEY, WEATHERSTACK_LOCATIONS,
    WTTRIN_LOCATIONS,
    QIWI_TOKEN, QIWI_CROSS_RATES,
    CBR_CROSS_RATES,
    BLOCKCHAIN_RATES,
    COVID_COUNTRIES, COVID_MODE,
    RSS_FEEDS, RSS_MAX_ENTRIES,
    TELEGRAM_API_TOKEN, TELEGRAM_USERS_ID
)
from api import (
    weatherstack, qiwi,
    rss, wttr_in, cbr_valutes,
    covid19, blockchain_rates
)
from registration import Registration, GlobalApi

if __name__ == "__main__":
    Registration(STARTING_MESSAGE, Registration.NetType.Telegram,
                 [GlobalApi(weatherstack.WeatherStack, [WEATHERSTACK_API_KEY, WEATHERSTACK_LOCATIONS]),
                  GlobalApi(wttr_in.WttrIn, [WTTRIN_LOCATIONS]),
                  GlobalApi(qiwi.Qiwi, [QIWI_TOKEN, QIWI_CROSS_RATES]),
                  GlobalApi(cbr_valutes.CbrValutes, [CBR_CROSS_RATES]),
                  GlobalApi(blockchain_rates.BlockchainRates, [BLOCKCHAIN_RATES]),
                  GlobalApi(covid19.Covid19, [COVID_COUNTRIES, COVID_MODE]),
                  GlobalApi(rss.RSS, [RSS_FEEDS, RSS_MAX_ENTRIES])]) \
        .init_net(TELEGRAM_API_TOKEN, TELEGRAM_USERS_ID) \
        .init_apis() \
        .send()
