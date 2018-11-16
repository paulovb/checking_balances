from unittest import TestCase
from unittest.mock import create_autospec

from api.usecases.see_balance import SeeBalance
from api.gateways.interfaces.financial_transaction_gateway import FinancialTransactionGateway
from api.gateways.interfaces.account_gateway import AccountGateway

from api.presenters.interfaces.financial_transaction_presenter import FinancialTransactionPresenter
from api.structs.financial_transaction import FinancialTransaction
from api.structs.account import Account

ACCOUNT_ID = 1

class SeeBalanceTests(TestCase):
    def setUp(self):
        self.account_gateway = create_autospec(AccountGateway)
        self.financial_transaction_gateway = create_autospec(FinancialTransactionGateway)
        self.financial_transaction_presenter = create_autospec(FinancialTransactionPresenter)

        self.usecase = SeeBalance(
            self.account_gateway,
            self.financial_transaction_gateway,
            self.financial_transaction_presenter
        )

    def test_see_balance_by_id(self):
        self.usecase.execute(ACCOUNT_ID)

        #self.financial_transaction_gateway.find_transactions_by_account_id.assert_called_once_with(ACCOUNT_ID)
