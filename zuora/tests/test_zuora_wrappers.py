import unittest
from unittest.mock import patch

from zuora.client import Zuora


class AccountTest(unittest.TestCase):
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

    @patch('zuora.wrappers.account.requests.get')
    def test_get_account(self, mock_get):
        zuora_account_key = 'A00003766'
        mock_get.return_value.json.return_value = expected = {
            'basicInfo': {
                'id': '402892c74c9193cd014c91d35b0a0132',
                'name': 'Test',
                'accountNumber': zuora_account_key,
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

        api_base = 'https://rest.apisandbox.zuora.com'
        zuora_settings = {
            'api_base': api_base,
            'username': 'pronto',
            'password': 'pronto',
        }
        zuora = Zuora(zuora_settings)
        result = zuora.account.get(zuora_account_key)

        self.assertDictEqual(result, expected)
        mock_get.assert_called_once_with(
            f'{api_base}/v1/accounts/{zuora_account_key}',
            headers={
                'apiAccessKeyId': 'pronto',
                'apiSecretAccessKey': 'pronto',
                'Content-Type': 'application/json'
            },
            verify=False
        )
