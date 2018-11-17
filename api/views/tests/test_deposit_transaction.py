import json
import urllib
from django.test import TestCase, Client
from api.models import FinancialTransaction
from api.models import Account


class DepositTests(TestCase):
    def setUp(self):
        self.request = Client()

    def assertFinancialTransaction(self, FinancialTransaction_expected, FinancialTransaction_founded):
        self.assertEqual(FinancialTransaction_expected.operation, FinancialTransaction_founded['operation'])
        self.assertEqual(FinancialTransaction_expected.notes, FinancialTransaction_founded['notes'])
        self.assertEqual(FinancialTransaction_expected.value, FinancialTransaction_founded['value'])
        self.assertEqual(FinancialTransaction_expected.last_balance, FinancialTransaction_founded['last_balance'])

    def test_deposit(self):
        account = Account.objects.create(name='Gabriela Lima', email='gabriela.lima@email.com', balance=23000.212)

        response = self.request.post(
            "/api/v1/deposit/",
            json.dumps({'value': 1100.405, 'account_id': account.id, 'notes': 'This is a deposit in account'}),
            content_type='application/json'
        )

        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(json.loads(response.content)['account_id'])

        deposit = FinancialTransaction.objects.all().last()
        
        self.assertEqual(1100.405, float(deposit.value))        
        self.assertEqual(23000.212, float(deposit.last_balance))
