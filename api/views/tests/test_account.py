import json
import urllib
from django.test import TestCase, Client
from api.models import Account


class AccountsTests(TestCase):
    def setUp(self):
        self.request = Client()

    def assertAccount(self, Account_expected, Account_founded):
        self.assertEqual(Account_expected.name, Account_founded['name'])
        self.assertEqual(Account_expected.email, Account_founded['email'])
        self.assertEqual(Account_expected.balance, Account_founded['balance'])
    
    def test_get_Account(self):
        account = Account.objects.create(name='Gabriela Lima', email='gabriela.lima@nubank.com', balance=5000.00)

        response = self.request.get("/api/v1/accounts/%s/" % account.id)

        self.assertEqual(200, response.status_code)
        content = json.loads(response.content)
        self.assertAccount(account, content)
    
    def test_create_Account(self):
        response = self.request.post(
            '/api/v1/accounts/',
            json.dumps({'name': 'Gabriela Lima', 'email': 'gabriela.lima@nubank.com', 'balance': 5000.00}),
            content_type='application/json'
        )

        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(json.loads(response.content)['id'])

        account_created = Account.objects.all()[0]

        self.assertEqual('Gabriela Lima', account_created.name)
        self.assertEqual('gabriela.lima@nubank.com', account_created.email)
        self.assertEqual(5000.00, account_created.balance)
    
    def test_update_Account(self):
        account = Account.objects.create(name='Gabriela Lima', email='gabriela.lima@nubank.com', balance=5000.00)

        response = self.request.put(
            '/api/v1/accounts/1/',
            json.dumps({'name': 'Gabriela Lima', 'email': 'gabriela.lima@nubank.com', 'balance': 5000.00}),
            content_type='application/json'
        )

        self.assertEqual(200, response.status_code)
        self.assertEqual(5000.00, Account.objects.get(id=account.id).balance)

    def test_delete_Account(self):
        account = Account.objects.create(name='Gabriela Lima', email='gabriela.lima@nubank.com', balance=5000.00)

        response = self.request.delete("/api/v1/accounts/%s/" % account.id)

        self.assertEqual(200, response.status_code)
        self.assertEqual(0, Account.objects.filter(id=account.id).count())
