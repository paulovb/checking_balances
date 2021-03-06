import json
import rollbar
from django.http.response import HttpResponse
from django.views.generic import View
from api.models import FinancialTransaction
from api.structs.financial_transaction import FinancialTransaction as FinancialTransactionStruct

from api.usecases.deposit_money import DepositMoney
from api.gateways.financial_transaction_gateway import FinancialTransactionGateway
from api.gateways.account_gateway import AccountGateway

from api.presenters.financial_transaction_presenter import FinancialTransactionPresenter
from api.structs.financial_transaction import FinancialTransaction
from api.structs.account import Account


class Deposit(View):

    def post(self, request):
        try:
            data = json.loads(request.body)

            presenter = FinancialTransactionPresenter()

            DepositMoney(
                AccountGateway(),
                FinancialTransactionGateway(),
                presenter
            ).execute(data["account_id"], float(data["value"]), data["notes"])

            return presenter.response()
        except:
            rollbar.report_exc_info()
