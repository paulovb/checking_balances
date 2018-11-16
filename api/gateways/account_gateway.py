from api.gateways.interfaces.account_gateway import AccountGateway as AccountGatewayInterface
from api.models import Account


class AccountGateway(AccountGatewayInterface):
    @staticmethod
    def get_by_id(account_id):
        return Account.objects.get(id=account_id)

    @staticmethod
    def update_balance(account_id, balance):
        account = Account.objects.get(id=account_id)
        account.balance = balance

        return account.save()
