class SeeBalance(object):
    def __init__(self, account_gateway, financial_transaction_gateway, financial_transaction_presenter):
        self.account_gateway = account_gateway
        self.financial_transaction_gateway = financial_transaction_gateway 
        self.financial_transaction_presenter = financial_transaction_presenter

    def execute(self, account_id):
        account = self.account_gateway.get_by_id(account_id)

        transactions = self.financial_transaction_gateway.find_transactions_by_account_id(account.id)

        self.financial_transaction_presenter.show(200, account, transactions)
