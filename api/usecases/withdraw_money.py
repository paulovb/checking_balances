class WithdrawMoney(object):
    def __init__(self, account_gateway, financial_transaction_gateway, financial_transaction_presenter):
        self.account_gateway = account_gateway
        self.financial_transaction_gateway = financial_transaction_gateway 
        self.financial_transaction_presenter = financial_transaction_presenter

    def execute(self, account_id, value, notes):
        account = self.account_gateway.get_by_id(account_id)

        if float(account.balance) < value:
            transactions = self.financial_transaction_gateway.find_transactions_by_account_id(account_id)

            return self.financial_transaction_presenter.show(203, account, transactions)

        self.financial_transaction_gateway.registry_withdraw_money(account_id, value)
        account = self.account_gateway.update_balance(account_id, account.balance - value, notes)

        transactions = self.financial_transaction_gateway.find_transactions_by_account_id(account_id)

        self.financial_transaction_presenter.show(200, account, transactions)
