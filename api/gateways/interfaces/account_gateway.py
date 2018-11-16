class AccountGateway(object):
    def get_by_id(self, account_id):
        raise NotImplementedError

    def update_balance(self, account_id, balance):
        raise NotImplementedError
