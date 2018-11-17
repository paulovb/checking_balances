import json
from unittest import TestCase
from api.presenters.financial_transaction_presenter import FinancialTransactionPresenter
from api.models import Account, FinancialTransaction


class FinancialTransactionPresenterTests(TestCase):
    def setUp(self):
        self.presenter = FinancialTransactionPresenter()

    def assertFinancialTransaction(self, transaction_expected, transaction_founded):
        self.assertEqual(transaction_expected.id, transaction_founded['account_id'])
        self.assertEqual(transaction_expected.name, transaction_founded['account_name'])
        self.assertEqual(transaction_expected.email, transaction_founded['account_email'])
        self.assertEqual(float(transaction_expected.balance), transaction_founded['account_balance'])

    def test_show_transactions(self):
        account = Account.objects.create(name='Gabriela Lima', email='gabriela.lima@email.com', balance=23000.212)

        financialTransaction_1 = FinancialTransaction.objects.create(operation='deposit', value=1000.503, last_balance=23000.212, account=account, notes='This is a deposit in account')
        financialTransaction_2 = FinancialTransaction.objects.create(operation='deposit', value=1000.504, last_balance=23000.213, account=account, notes='This is a deposit in account')
    
        transactions = [financialTransaction_1, financialTransaction_2]

        self.presenter.show(200, account, transactions)

        response = self.presenter.response()

        self.assertEqual(200, response.status_code)
        content = json.loads(response.content)

        self.assertEqual(2, len(content["transactions"]))
