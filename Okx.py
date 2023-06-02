import loguru
import requests
import time
import requests


with open("Config.txt", "r") as f:

    config = [row.split() for row in f]


done = []
while len(done) != len(config):


    try:
        for cfg in config:

            headers = {
                'authorization': f'{cfg[0]}','content-type': 'application/json','origin': 'https://www.okx.cab','referer': 'https://www.okx.cab/ru/trade-spot/usdt-usdc','sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','timeout': '10000','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36','x-cdn': 'https://static.okx.cab','x-locale': 'ru_RU','x-utc': '5','authority': 'www.okx.cab','accept': 'application/json','accept-language': 'ru-RU','app-type': 'web',
            }

            params = {
                't': f'{time.time()}',
            }

            json_data = {
                'instId': 'SUI-USDT',
                'tdMode': 'cash',
                '_feReq': True,
                'side': 'sell',
                'ordType': 'market',
                'sz': f'{cfg[1]}',
            }

            response = requests.post(
                'https://www.okx.cab/priapi/v5/trade/order',
                params=params,
                headers=headers,
                json=json_data,
            )


            if response.json()['code'] == "0":
                loguru.logger.success(response.json()['data'][0]['sMsg'])
                done.append("Done")
            else:
                loguru.logger.info("Ждём токены")
    except:
        loguru.logger.error("ОШИБКА")