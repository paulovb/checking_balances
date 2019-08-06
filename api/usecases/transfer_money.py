class TransferMoney(object):
    def __init__(self, account_gateway, financial_transaction_gateway, financial_transaction_presenter):
        self.account_gateway = account_gateway
        self.financial_transaction_gateway = financial_transaction_gateway 
        self.financial_transaction_presenter = financial_transaction_presenter

    def execute(self, account_withdraw_id, account_deposit_id, value, notes):

        account_withdraw = self.account_gateway.get_by_id(account_withdraw_id)

        if float(account_withdraw.balance) < value:
            transactions = self.financial_transaction_gateway.find_transactions_by_account_id(account_withdraw_id)

            return self.financial_transaction_presenter.show(203, account_withdraw, transactions)

        self.financial_transaction_gateway.registry_withdraw_money(account_withdraw_id, value, notes)
        account_withdraw = self.account_gateway.update_balance(account_withdraw_id, float(account_withdraw.balance) - float(value))

        account_deposit = self.account_gateway.get_by_id(account_deposit_id)

        self.financial_transaction_gateway.registry_deposit_money(account_deposit_id, value, notes)
        account_deposit = self.account_gateway.update_balance(account_deposit_id, float(account_deposit.balance) + float(value))

        transactions = self.financial_transaction_gateway.find_transactions_by_account_id(account_withdraw_id)
        
        account_withdraw = self.account_gateway.get_by_id(account_withdraw_id)

        self.financial_transaction_presenter.show(201, account_withdraw, transactions)

        
        self.financial_transaction_gateway.registry_deposit_money(account_deposit_id, value, notes)
        account_deposit = self.account_gateway.update_balance(account_deposit_id, float(account_deposit.balance) + float(value))

        transactions = self.financial_transaction_gateway.find_transactions_by_account_id(account_withdraw_id)
        
        account_withdraw = self.account_gateway.get_by_id(account_withdraw_id)

        self.financial_transaction_presenter.show(201, account_withdraw, transactions)

