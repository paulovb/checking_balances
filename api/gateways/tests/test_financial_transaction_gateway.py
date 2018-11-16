from django.test import TestCase
from django.db.utils import DataError

from api.models import Account, FinancialTransaction
from api.gateways.financial_transaction_gateway import FinancialTransactionGateway


class FinancialTransactionGatewayTests(TestCase):
    def setUp(self):
        pass

    def test_find_transactions_by_account_id(self):

        account = Account.objects.create(name='Gabriela Lima', email='gabriela.lima@nubank.com', balance=23000.212)

        financialTransaction_1 = FinancialTransaction.objects.create(operation='deposit', value=1000.503, last_balance=23000.212, account=account, notes='This is a deposit in account')
        financialTransaction_2 = FinancialTransaction.objects.create(operation='deposit', value=1000.504, last_balance=23000.213, account=account, notes='This is a deposit in account')

        transactions = FinancialTransactionGateway.find_transactions_by_account_id(account.id)

        self.assertEqual(2, len(transactions))
