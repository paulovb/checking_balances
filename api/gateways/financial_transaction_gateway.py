import json
from api.models import FinancialTransaction
from api.gateways.interfaces.financial_transaction_gateway import FinancialTransactionGateway as FinancialTransactionGatewayInterface


class FinancialTransactionGateway(FinancialTransactionGatewayInterface):
    @staticmethod
    def find_transactions_by_account_id(account_id):
    	return list(FinancialTransaction.objects.all().filter(account_id=account_id))
