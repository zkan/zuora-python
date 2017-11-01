import requests


class Account(object):
    def __init__(self, zuora_settings):
        self.zuora_settings = zuora_settings

    def get(self, zuora_account_key):
        url = f'{self.zuora_settings.get("api_base")}' \
            f'/v1/accounts/{zuora_account_key}'
        response = requests.get(
            url,
            headers=self.zuora_settings.get('headers'),
            verify=self.zuora_settings.get('verify_ssl_certs')
        )
        return response.json()
