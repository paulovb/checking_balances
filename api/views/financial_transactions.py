import json
from django.http.response import HttpResponse
from django.views.generic import View
from api.models import FinancialTransaction
from api.structs.financial_transaction import FinancialTransaction as FinancialTransactionStruct

class FinancialTransactions(View):
    
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
