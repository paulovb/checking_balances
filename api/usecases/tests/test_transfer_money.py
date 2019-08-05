from unittest import TestCase
from unittest.mock import create_autospec

from api.usecases.transfer_money import TransferMoney
from api.gateways.interfaces.financial_transaction_gateway import FinancialTransactionGateway
from api.gateways.interfaces.account_gateway import AccountGateway

from api.presenters.interfaces.financial_transaction_presenter import FinancialTransactionPresenter
from api.structs.financial_transaction import FinancialTransaction
from api.structs.account import Account

ACCOUNT_ID_WITHDRAW = 1
ACCOUNT_ID_DEPOSIT = 2
VALUE = 2500.123
NOTES = "Transfer"

class TransferMoneyTests(TestCase):
    def setUp(self):
        self.account_gateway = create_autospec(AccountGateway)
        self.financial_transaction_gateway = create_autospec(FinancialTransactionGateway)
        self.financial_transaction_presenter = create_autospec(FinancialTransactionPresenter)

        self.usecase = TransferMoney(
            self.account_gateway,
            self.financial_transaction_gateway,
            self.financial_transaction_presenter
        )

    def test_transfer_money_by_person_one_to_person_two_by_account_id(self):
        self.usecase.execute(ACCOUNT_ID_WITHDRAW, ACCOUNT_ID_DEPOSIT, VALUE, NOTES)

