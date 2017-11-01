from zuora.wrappers import (
    Account,
    Subscription
)


class Zuora(object):
    def __init__(self, zuora_settings):
        if zuora_settings.get('api_base'):
            self.api_base = zuora_settings.get('api_base')
        else:
            self.api_base = 'https://rest.zuora.com'

        self.verify_ssl_certs = False
        self.headers = {
            'apiAccessKeyId': zuora_settings.get('username'),
            'apiSecretAccessKey': zuora_settings.get('password'),
            'Content-Type': 'application/json'
        }

        zuora_settings['api_base'] = self.api_base
        zuora_settings['verify_ssl_certs'] = self.verify_ssl_certs
        zuora_settings['headers'] = self.headers

        self.account = Account(zuora_settings)
        self.subscription = Subscription(zuora_settings)
