from django.conf.urls import url
from api.views.accounts import Accounts


urlpatterns = [
    url(r'^v1/accounts/$', Accounts.as_view()),
    url(r'^v1/accounts/(?P<account_id>\d+)/$', Accounts.as_view()),
]
