import json
import urllib
from django.test import TestCase, Client
from api.models import FinancialTransaction
from api.models import Account


class FinancialTransactionsTests(TestCase):
    def setUp(self):
        self.request = Client()

    def assertFinancialTransaction(self, FinancialTransaction_expected, FinancialTransaction_founded):
        self.assertEqual(FinancialTransaction_expected.operation, FinancialTransaction_founded['operation'])
        self.assertEqual(FinancialTransaction_expected.notes, FinancialTransaction_founded['notes'])
        self.assertEqual(FinancialTransaction_expected.value, FinancialTransaction_founded['value'])
        self.assertEqual(FinancialTransaction_expected.last_balance, FinancialTransaction_founded['last_balance'])
    
    def test_get_financial_transaction(self):

        account = Account.objects.create(name='Gabriela Lima', email='gabriela.lima@nubank.com', balance=23000.212)

        financialTransaction = FinancialTransaction.objects.create(operation='deposit', value=1000.503, last_balance=23000.212, account=account, notes='This is a deposit in account')

        response = self.request.get("/api/v1/financial_transaction/%s/" % financialTransaction.id)

        self.assertEqual(200, response.status_code)
        content = json.loads(response.content)
        self.assertFinancialTransaction(financialTransaction, content)

    def test_create_FinancialTransaction(self):
        account = Account.objects.create(name='Gabriela Lima', email='gabriela.lima@nubank.com', balance=23000.212)

        response = self.request.post(
            "/api/v1/financial_transaction/",
            json.dumps({'value': 1100.405, 'last_balance': 23100.114, 'account_id': account.id, 'notes': 'This is a deposit in account'}),
            content_type='application/json'
        )

        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(json.loads(response.content)['id'])

        self.assertEqual(1100.405, float(FinancialTransaction.objects.get(id=json.loads(response.content)['id']).value))        
        self.assertEqual(23100.114, float(FinancialTransaction.objects.get(id=json.loads(response.content)['id']).last_balance))

    def test_update_FinancialTransaction(self):
        account = Account.objects.create(name='Gabriela Lima', email='gabriela.lima@nubank.com', balance=23000.212)

        financialTransaction = FinancialTransaction.objects.create(operation='deposit', value=1000.503, last_balance=23000.212, account=account, notes='This is a deposit in account')

        response = self.request.put(
            "/api/v1/financial_transaction/%s/" % financialTransaction.id,
            json.dumps({'value': 1100.405, 'last_balance': 23100.114}),
            content_type='application/json'
        )

        self.assertEqual(200, response.status_code)
        self.assertEqual(1100.405, float(FinancialTransaction.objects.get(id=financialTransaction.id).value))
        self.assertEqual(23100.114, float(FinancialTransaction.objects.get(id=financialTransaction.id).last_balance))

    def test_delete_FinancialTransaction(self):
        account = Account.objects.create(name='Gabriela Lima', email='gabriela.lima@nubank.com', balance=23000.212)

        financialTransaction = FinancialTransaction.objects.create(operation='deposit', value=1000.503, last_balance=23000.212, account=account, notes='This is a deposit in account')

        response = self.request.delete("/api/v1/financial_transaction/%s/" % financialTransaction.id)

        self.assertEqual(200, response.status_code)
        self.assertEqual(0, FinancialTransaction.objects.filter(id=financialTransaction.id).count())
