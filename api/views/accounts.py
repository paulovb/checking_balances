import json
import rollbar
from django.http.response import HttpResponse
from django.views.generic import View
from api.models import Account
from api.structs.account import Account as AccountStruct


class Accounts(View):

    def get(self, _, account_id=None):
        try:
            if account_id:
                account = Account.objects.get(id=account_id)

                return HttpResponse(
                    json.dumps(
                        AccountStruct(
                            id=account.id,
                            name=account.name,
                            email=account.email,
                            balance=float(account.balance)).__dict__),
                    content_type='application/json')
            else:
                accounts = Account.objects.all()

                return HttpResponse(
                    json.dumps(
                        [AccountStruct(
                            id=account.id,
                            name=account.name,
                            email=account.email,
                            balance=float(account.balance)).__dict__ for account in accounts]),
                    content_type='application/json')
        except:
            rollbar.report_exc_info()

    def post(self, request):
        try:
            data = json.loads(request.body)
            account = Account(**data)
            account.save()

            return HttpResponse(
                status=201,
                content=json.dumps({
                    'id': account.id
                }),
                content_type='application/json')
        except:
            rollbar.report_exc_info()

    def put(self, request, account_id):
        try:
            data = json.loads(request.body)
            Account.objects.filter(id=account_id).update(**data)
            return HttpResponse()
        except:
            rollbar.report_exc_info()

    def delete(self, r_, account_id):
        try:
            Account.objects.filter(id=account_id).delete()
            return HttpResponse()
        except:
            rollbar.report_exc_info()
