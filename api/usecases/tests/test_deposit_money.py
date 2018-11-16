from unittest import TestCase
from unittest.mock import create_autospec

ACCOUNT_ID = 1

class DepositMoneyByAccountTests(TestCase):
    def setUp(self):
        self.financial_transaction_gateway = create_autospec(FinancialTransactionGateway)
        self.account_gateway = create_autospec(AccountGateway)
        self.financial_transaction_presenter = create_autospec(FinancialTransactionPresenter)

        self.usecase = DepositMoney(
            self.financial_transaction_gateway,
            self.account_gateway,
            self.financial_transaction_presenter
        )

    def test_deposit_money_by_id(self):
        self.usecase.execute(ACCOUNT_ID)

        self.financial_transactions_gateway.get_by_id.assert_called_once_with(ACCOUNT_ID)


