from config import (
    STARTING_MESSAGE,
    weatherstack_config, wttrin_config,
    qiwi_config, cbr_config,
    blockchain_config, covid19_config,
    rss_config,
    TELEGRAM_API_TOKEN, TELEGRAM_USERS_ID
)
from api.service_apis import weatherstack, qiwi, blockchain_rates, wttr_in, rss, covid19, cbr_valutes
from service.registration import ApisList, SocialNet, SocialNetType

if __name__ == "__main__":

    apis = ApisList()
    #apis.add_api(weatherstack.WeatherStack(weatherstack_config))
    apis.add_api(wttr_in.WttrIn(wttrin_config))
    #add_api(qiwi.Qiwi(qiwi_config))
    apis.add_api(cbr_valutes.CbrValutes(cbr_config))
    apis.add_api(blockchain_rates.BlockchainRates(blockchain_config))
    apis.add_api(covid19.Covid19(covid19_config))
    apis.add_api(rss.RSS(rss_config))

    message = f"{STARTING_MESSAGE}{apis.get_str()}"

    telegram_net = SocialNet(SocialNetType.Telegram, TELEGRAM_API_TOKEN)
    telegram_net.send(message, TELEGRAM_USERS_ID)
