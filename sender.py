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
from api.service_apis import weatherstack, qiwi, blockchain_rates, wttr_in, rss, covid19, cbr_valutes
from service.registration import ApisList, SocialNet, SocialNetType

if __name__ == "__main__":

    apis = ApisList()
    apis.add_api(weatherstack.WeatherStack, [WEATHERSTACK_API_KEY, WEATHERSTACK_LOCATIONS])
    apis.add_api(wttr_in.WttrIn, [WTTRIN_LOCATIONS])
    apis.add_api(qiwi.Qiwi, [QIWI_TOKEN, QIWI_CROSS_RATES])
    apis.add_api(cbr_valutes.CbrValutes, [CBR_CROSS_RATES])
    apis.add_api(blockchain_rates.BlockchainRates, [BLOCKCHAIN_RATES])
    apis.add_api(covid19.Covid19, [COVID_COUNTRIES, COVID_MODE])
    apis.add_api(rss.RSS, [RSS_FEEDS, RSS_MAX_ENTRIES])

    message = f"{STARTING_MESSAGE}{apis.get_str()}"

    telegram_net = SocialNet(SocialNetType.Telegram, TELEGRAM_API_TOKEN)
    telegram_net.send(message, TELEGRAM_USERS_ID)
