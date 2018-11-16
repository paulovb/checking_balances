from api.gateways.interfaces.account_gateway import AccountGateway as AccountGatewayInterface
from api.models import Account


class AccountGateway(AccountGatewayInterface):
    def get_by_id(self, account_id):
        return Account.objects.get(id=account_id)
