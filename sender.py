from api.social_nets.telegram import Telegram
from api.social_nets.vkontakte import Vkontakte
from config import (
    STARTING_MESSAGE,
    weatherstack_config, wttrin_config,
    qiwi_config, cbr_config,
    blockchain_config, covid19_config,
    rss_config,
    TELEGRAM_API_TOKEN, TELEGRAM_USERS_ID,
    VK_API_TOKEN, VK_USERS_ID
)
from api.service_apis import weatherstack, qiwi, blockchain_rates, wttr_in, rss, covid19, cbr_valutes
from service.registration import ApisList

if __name__ == "__main__":

    apis = ApisList()

    if weatherstack_config:
        apis.add_api(weatherstack.WeatherStack(weatherstack_config))
    if wttrin_config:
        apis.add_api(wttr_in.WttrIn(wttrin_config))
    if qiwi_config:
        apis.add_api(qiwi.Qiwi(qiwi_config))
    if cbr_config:
        apis.add_api(cbr_valutes.CbrValutes(cbr_config))
    if blockchain_config:
        apis.add_api(blockchain_rates.BlockchainRates(blockchain_config))
    if covid19_config:
        apis.add_api(covid19.Covid19(covid19_config))
    if rss_config:
        apis.add_api(rss.RSS(rss_config))

    message = f"{STARTING_MESSAGE}{apis}"

    if TELEGRAM_API_TOKEN and TELEGRAM_USERS_ID:
        tg = Telegram(TELEGRAM_API_TOKEN)
        tg.send(message, TELEGRAM_USERS_ID)

    if VK_API_TOKEN and VK_USERS_ID:
        vk = Vkontakte(VK_API_TOKEN)
        vk.send(message, VK_USERS_ID)
