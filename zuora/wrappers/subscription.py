import requests


class Subscription(object):
    def __init__(self, zuora_settings):
        self.zuora_settings = zuora_settings

    def create(self, data):
        url = f'{self.zuora_settings.get("api_base")}' \
            f'/v1/subscriptions'
        response = requests.post(
            url,
            headers=self.zuora_settings.get('headers'),
            json=data,
            verify=self.zuora_settings.get('verify_ssl_certs')
        )
        return response.json()
