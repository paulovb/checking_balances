import json
from django.http.response import HttpResponse
from django.views.generic import View
from api.models import FinancialTransaction
from api.structs.financial_transaction import FinancialTransaction as FinancialTransactionStruct

class FinancialTransactions(View):

    def get(self, _, financialTransaction_id=None):

        if financialTransaction_id:
            financialTransaction = FinancialTransaction.objects.get(id=financialTransaction_id)

            return HttpResponse(
                json.dumps(
                    FinancialTransactionStruct(
                        operation=financialTransaction.operation, 
                        notes=financialTransaction.notes, 
                        value=float(financialTransaction.value),
                        last_balance=float(financialTransaction.last_balance)).__dict__),
                content_type='application/json')
        else:
            financialTransactions = FinancialTransaction.objects.all()

            return HttpResponse(
                json.dumps(
                    [FinancialTransactionStruct(
                        operation=financialTransaction.operation, 
                        notes=financialTransaction.notes, 
                        value=float(financialTransaction.value),
                        last_balance=float(financialTransaction.last_balance)).__dict__ for financialTransaction in financialTransactions]),
                content_type='application/json')
    
    def post(self, request):
        data = json.loads(request.body)
        financialTransaction = FinancialTransaction(**data)
        financialTransaction.save()

        return HttpResponse(
            status=201, 
            content=json.dumps({
                'id': financialTransaction.id
            }),
            content_type='application/json')

    def put(self, request, financialTransaction_id):
        data = json.loads(request.body)
        FinancialTransaction.objects.filter(id=financialTransaction_id).update(**data)
        return HttpResponse()

    def delete(self, r_, financialTransaction_id):
        FinancialTransaction.objects.filter(id=financialTransaction_id).delete()
        return HttpResponse()
