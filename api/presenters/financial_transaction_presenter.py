import json
from django.http.response import HttpResponse
from api.presenters.interfaces.financial_transaction_presenter import FinancialTransactionPresenter as FinancialTransactionPresenterInterface


class FinancialTransactionPresenter(FinancialTransactionPresenterInterface):
    def __init__(self):
        self.content_account = {}
        self.content_transactions = []

    def show(self, account, transactions):

        self.content_account = {
            'account_id': account.id,
            'account_name': account.name,
            'account_email': account.email,
            'account_balance': account.balance,
        }

        for transaction in transactions:
            self.content_transactions.append({
                'operation': transaction.operation,
                'value': transaction.value,
#                'date': transaction.created_at,
            })

        if self.content_transactions:
            self.content_account.update({'transactions': self.content_transactions})

    def response(self):
        return HttpResponse(
            content=json.dumps(self.content_account),
            content_type='application/json'
        )
 