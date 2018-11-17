import json
import urllib
from django.test import TestCase, Client
from api.models import FinancialTransaction
from api.models import Account


class WithdrawTests(TestCase):
    def setUp(self):
        self.request = Client()

    def assertFinancialTransaction(self, FinancialTransaction_expected, FinancialTransaction_founded):
        self.assertEqual(FinancialTransaction_expected.operation, FinancialTransaction_founded['operation'])
        self.assertEqual(FinancialTransaction_expected.notes, FinancialTransaction_founded['notes'])
        self.assertEqual(FinancialTransaction_expected.value, FinancialTransaction_founded['value'])
        self.assertEqual(FinancialTransaction_expected.last_balance, FinancialTransaction_founded['last_balance'])

    def test_withdraw_with_enough_money(self):
        account = Account.objects.create(name='Gabriela Lima', email='gabriela.lima@email.com', balance=23000.212)

        response = self.request.post(
            "/api/v1/withdraw/",
            json.dumps({'value': 100.000, 'account_id': account.id, 'notes': 'This is a withdraw in account'}),
            content_type='application/json'
        )

        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(json.loads(response.content)['account_id'])

        withdraw = FinancialTransaction.objects.all().last()
        
        self.assertEqual(100.000, float(withdraw.value))        
        self.assertEqual(23000.212, float(withdraw.last_balance))

    def test_withdraw_without_enough_money(self):
        account = Account.objects.create(name='Gabriela Lima', email='gabriela.lima@email.com', balance=23000.212)

        response = self.request.post(
            "/api/v1/withdraw/",
            json.dumps({'value': 25000.000, 'account_id': account.id, 'notes': 'This is a withdraw in account'}),
            content_type='application/json'
        )

        self.assertEqual(203, response.status_code)
