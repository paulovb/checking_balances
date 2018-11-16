import json
from django.http.response import HttpResponse
from api.presenters.interfaces.financial_transaction_presenter import FinancialTransactionPresenter as FinancialTransactionPresenterInterface


class FinancialTransactionPresenter(FinancialTransactionPresenterInterface):
    def __init__(self):
        self.content_account = {}
        self.content_transactions = []
        self.status = 201

    def show(self, status, account, transactions):

        self.status = status

        self.content_account = {
            'account_id': account.id,
            'account_name': account.name,
            'account_email': account.email,
            'account_balance': float(account.balance),
        }

        for transaction in transactions:
            self.content_transactions.append({
                'transaction_id': transaction.id,
                'operation': transaction.operation,
                'date': str(transaction.created_at),
                'value': float(transaction.value),
                'last_balance': float(transaction.last_balance),
                'notes': transaction.notes,
            })

        if self.content_transactions:
            self.content_account.update({'transactions': self.content_transactions})

    def response(self):
        return HttpResponse(
            status=self.status,
            content=json.dumps(self.content_account),
            content_type='application/json'
        )
 