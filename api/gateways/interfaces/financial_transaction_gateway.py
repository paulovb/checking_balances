class FinancialTransactionGateway(object):
    def find_transactions_by_account_id(self, segmentation_id):
        raise NotImplementedError

    def registry_deposit_money(self, account_id, value, notes):
        raise NotImplementedError

    def registry_withdraw_money(self, account_id, value, notes):
       raise NotImplementedError
