import json
import rollbar
from django.http.response import HttpResponse
from django.views.generic import View

from api.usecases.see_balance import SeeBalance
from api.gateways.financial_transaction_gateway import FinancialTransactionGateway
from api.gateways.account_gateway import AccountGateway

from api.presenters.financial_transaction_presenter import FinancialTransactionPresenter
from api.structs.financial_transaction import FinancialTransaction
from api.structs.account import Account


class Balance(View):

    def get(self, _, account_id):
        try:
            presenter = FinancialTransactionPresenter()

            SeeBalance(
                AccountGateway(),
                FinancialTransactionGateway(),
                presenter
            ).execute(account_id)

            return presenter.response()
        except:
            rollbar.report_exc_info()
