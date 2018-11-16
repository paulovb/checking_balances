from django.conf.urls import url
from api.views.accounts import Accounts
from api.views.financial_transactions import FinancialTransactions


urlpatterns = [
    url(r'^v1/accounts/$', Accounts.as_view()),
    url(r'^v1/accounts/(?P<account_id>\d+)/$', Accounts.as_view()),
    url(r'^v1/financial_transaction/$', FinancialTransactions.as_view()),
    url(r'^v1/financial_transaction/(?P<financialTransaction_id>\d+)/$', FinancialTransactions.as_view()),
]
