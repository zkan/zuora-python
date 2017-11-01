from zuora.client import Zuora
from zuora.tests.helper import ZuoraTestCase


class AccountTest(ZuoraTestCase):
    def test_get_account(self):
        zuora = Zuora({})
        result = zuora.account.get('A00003766')
        self.assertDictEqual(result, {})
