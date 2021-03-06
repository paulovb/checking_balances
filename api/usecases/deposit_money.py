class DepositMoney(object):
    def __init__(self, account_gateway, financial_transaction_gateway, financial_transaction_presenter):
        self.account_gateway = account_gateway
        self.financial_transaction_gateway = financial_transaction_gateway 
        self.financial_transaction_presenter = financial_transaction_presenter

    def execute(self, account_id, value, notes):
        account = self.account_gateway.get_by_id(account_id)

        self.financial_transaction_gateway.registry_deposit_money(account_id, value, notes)
        account = self.account_gateway.update_balance(account_id, float(account.balance) + float(value))

        transactions = self.financial_transaction_gateway.find_transactions_by_account_id(account_id)

        account = self.account_gateway.get_by_id(account_id)

        self.financial_transaction_presenter.show(201, account, transactions)
