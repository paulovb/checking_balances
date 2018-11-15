from unittest import TestCase
from unittest.mock import create_autospec


class DepositMoneyByAccountTests(TestCase):
    def setUp(self):
        self.financial_transactions_gateway = create_autospec(FinancialTransactionsGateway)
        self.account_gateway = create_autospec(AccountGateway)
        self.financial_transactions_presenter = create_autospec(FinancialTransactionsPresenter)

        self.usecase = DepositMoney(
            self.financial_transactions_gateway,
            self.account_gateway,
            self.financial_transactions_presenter
        )

