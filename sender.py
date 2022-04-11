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
    configs = [weatherstack_config,
               wttrin_config, qiwi_config,
               cbr_config, blockchain_config,
               covid19_config, rss_config]

    for config in configs:
        if config:
            apis.add_api(config.base_class(config))

    message = f"{STARTING_MESSAGE}{apis}"

    if TELEGRAM_API_TOKEN and TELEGRAM_USERS_ID:
        tg = Telegram(TELEGRAM_API_TOKEN)
        tg.send(message, TELEGRAM_USERS_ID)

    if VK_API_TOKEN and VK_USERS_ID:
        vk = Vkontakte(VK_API_TOKEN)
        vk.send(message, VK_USERS_ID)
