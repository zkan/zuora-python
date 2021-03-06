import unittest
from unittest.mock import patch

from zuora.client import Zuora


class ZuoraSettingsTest(unittest.TestCase):
    def test_zuora_settings(self):
        zuora_settings = {
            'username': 'pronto',
            'password': 'pronto',
        }
        zuora = Zuora(zuora_settings)

        self.assertEqual(zuora.api_base, 'https://rest.zuora.com')
        expected_headers = {
            'apiAccessKeyId': 'pronto',
            'apiSecretAccessKey': 'pronto',
            'Content-Type': 'application/json'
        }
        self.assertDictEqual(zuora.headers, expected_headers)
        self.assertFalse(zuora.verify_ssl_certs)


class AccountTest(unittest.TestCase):
    def setUp(self):
        self.zuora_account_key = 'A00003766'
        self.api_base = 'https://rest.apisandbox.zuora.com'
        zuora_settings = {
            'api_base': self.api_base,
            'username': 'pronto',
            'password': 'pronto',
        }
        self.zuora = Zuora(zuora_settings)

    @patch('zuora.wrappers.account.requests.get')
    def test_get_account(self, mock_get):
        mock_get.return_value.json.return_value = expected = {
            'basicInfo': {
                'id': '402892c74c9193cd014c91d35b0a0132',
                'name': 'Test',
                'accountNumber': self.zuora_account_key,
                'notes': '',
                'status': 'Active',
                'crmId': '',
                'batch': 'Batch1',
                'invoiceTemplateId': None,
                'communicationProfileId': '303d186840e611df817c002185d714e1'
            },
            'billingAndPayment': {
                'billCycleDay': 1,
                'currency': 'USD',
                'paymentTerm': 'Net 30',
                'paymentGateway': 'TestGateway',
                'invoiceDeliveryPrefsPrint': False,
                'invoiceDeliveryPrefsEmail': True,
                'additionalEmailAddresses': [
                    'test1@test.com',
                    'test2@test.com'
                ]
            },
            'metrics': {
                'balance': 0,
                'totalInvoiceBalance': 0,
                'creditBalance': 0,
                'contractedMrr': -900
            },
            'billToContact': {
                'address1': '',
                'address2': '',
                'city': '',
                'country': None,
                'county': None,
                'fax': '',
                'firstName': 'Test',
                'homePhone': '',
                'lastName': 'Test',
                'mobilePhone': '',
                'nickname': '',
                'otherPhone': '',
                'otherPhoneType': None,
                'personalEmail': '',
                'state': '',
                'taxRegion': None,
                'workEmail': 'Test@test.com',
                'workPhone': '',
                'zipCode': ''
            },
            'soldToContact': {
                'address1': '',
                'address2': '',
                'city': '',
                'country': None,
                'county': None,
                'fax': '',
                'firstName': 'Test',
                'homePhone': '',
                'lastName': 'Test',
                'mobilePhone': '',
                'nickname': '',
                'otherPhone': '',
                'otherPhoneType': None,
                'personalEmail': '',
                'state': '',
                'taxRegion': None,
                'workEmail': 'Test@test.com',
                'workPhone': '',
                'zipCode': ''
            },
            'success': True
        }

        result = self.zuora.account.get(self.zuora_account_key)

        self.assertDictEqual(result, expected)
        mock_get.assert_called_once_with(
            f'{self.api_base}/v1/accounts/{self.zuora_account_key}',
            headers={
                'apiAccessKeyId': 'pronto',
                'apiSecretAccessKey': 'pronto',
                'Content-Type': 'application/json'
            },
            verify=False
        )

    @patch('zuora.wrappers.account.requests.post')
    def test_create_account(self, mock_post):
        mock_post.return_value.json.return_value = expected = {
            'success': True,
            'accountId': '402892c74c9193cd014c96bbe7c101f9',
            'accountNumber': 'A00000004',
            'paymentMethodId': '402892c74c9193cd014c96bbe7d901fd'
        }

        account_data = {
            'additionalEmailAddresses': [
                'test1@test.com',
                'test2@test.com'
            ],
            'autoPay': False,
            'billCycleDay': 0,
            'billToContact': {
                'address1': '1051 E Hillsdale Blvd',
                'city': 'Foster City',
                'country': 'United States',
                'firstName': 'John',
                'lastName': 'Smith',
                'state': 'CA',
                'workEmail': 'john.smith@test.com',
                'zipCode': '94404'
            },
            'currency': 'USD',
            'creditCard': {
                'cardType': 'Visa',
                'cardNumber': '4111111111111111',
                'expirationMonth': '2',
                'expirationYear': '2014',
                'cardHolderInfo': {
                    'cardHolderName': 'Kan Ouivirach',
                    'addressLine1': 'Somewhere',
                    'city': 'Bangkok',
                    'state': 'Somewhere in Bangkok',
                    'zipCode': '12000',
                    'country': 'Thailand',
                    'email': 'kan@prontomarketing.com'
                }
            },
            'invoiceDeliveryPrefsEmail': True,
            'invoiceDeliveryPrefsPrint': False,
            'name': 'Zuora Test Account',
            'notes': 'This account is for demo purposes.',
            'paymentTerm': 'Due Upon Receipt'
        }
        result = self.zuora.account.create(account_data)

        self.assertDictEqual(result, expected)
        mock_post.assert_called_once_with(
            f'{self.api_base}/v1/accounts',
            headers={
                'apiAccessKeyId': 'pronto',
                'apiSecretAccessKey': 'pronto',
                'Content-Type': 'application/json'
            },
            json=account_data,
            verify=False
        )


class SubscriptionTest(unittest.TestCase):
    def setUp(self):
        self.zuora_account_key = 'A00003766'
        self.api_base = 'https://rest.apisandbox.zuora.com'
        zuora_settings = {
            'api_base': self.api_base,
            'username': 'pronto',
            'password': 'pronto',
        }
        self.zuora = Zuora(zuora_settings)

    @patch('zuora.wrappers.subscription.requests.post')
    def test_create_subscription(self, mock_post):
        mock_post.return_value.json.return_value = expected = {
            'subscriptionNumber': 'A-S00001084',
            'success': True,
            'subscriptionId': '2c92c8f83dcbd8b1013dcce0ead40071'
        }

        subscription_data = {
            'accountKey': 'A00004268',
            'termType': 'EVERGREEN',
            'contractEffectiveDate': '2014-01-01',
            'serviceActivationDate': '2014-01-01',
            'invoiceCollect': 'true',
            'subscribeToRatePlans': [
                {
                    'productRatePlanId': '4028e6962eb8004a012ed83fa9fd241e'
                }
            ]
        }
        result = self.zuora.subscription.create(subscription_data)

        self.assertDictEqual(result, expected)
        mock_post.assert_called_once_with(
            f'{self.api_base}/v1/subscriptions',
            headers={
                'apiAccessKeyId': 'pronto',
                'apiSecretAccessKey': 'pronto',
                'Content-Type': 'application/json'
            },
            json=subscription_data,
            verify=False
        )
