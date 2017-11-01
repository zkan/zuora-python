from zuora.wrappers import Account


class Zuora(object):
    def __init__(self, zuora_settings):
        self.api_base = 'https://api.zuora.com'
        self.verify_ssl_certs = False
        self.headers = {
            'apiAccessKeyId': zuora_settings.get('username'),
            'apiSecretAccessKey': zuora_settings.get('password'),
            'Content-Type': 'application/json'
        }
        self.account = Account(zuora_settings)
