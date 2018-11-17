from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    balance = models.DecimalField(decimal_places=3,max_digits=25,default=0.000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
       managed = True
       db_table = 'account'

class FinancialTransaction(models.Model):
    operation = models.CharField(max_length=255)
    notes = models.TextField()
    value = models.DecimalField(decimal_places=3,max_digits=25,default=0.000)
    last_balance = models.DecimalField(decimal_places=3,max_digits=25,default=0.000)
    created_at = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
       managed = True
       db_table = 'financial_transactions'
