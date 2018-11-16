import json
from api.models import Account, FinancialTransaction
from api.gateways.interfaces.financial_transaction_gateway import FinancialTransactionGateway as FinancialTransactionGatewayInterface


class FinancialTransactionGateway(FinancialTransactionGatewayInterface):
    @staticmethod
    def find_transactions_by_account_id(account_id):
        return list(FinancialTransaction.objects.all().filter(account_id=account_id))

    @staticmethod
    def registry_deposit_money(account_id, value, notes):
        account = Account.objects.get(id=account_id)

        financialTransaction = FinancialTransaction.objects.create(operation='deposit', value=value, last_balance=account.balance, account=account, notes=notes)

        return financialTransaction

    @staticmethod
    def registry_withdraw_money(account_id, value, notes):
        account = Account.objects.get(id=account_id)

        financialTransaction = FinancialTransaction.objects.create(operation='deposit', value=value, last_balance=account.balance, account=account, notes=notes)

        return financialTransaction
