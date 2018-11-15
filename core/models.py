from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    balance = models.DecimalField(decimal_places=3,max_digits=25)

class FinancialTransactions(models.Model):
    operation = models.CharField(max_length=255)
    notes = models.TextField()
    value = models.DecimalField(decimal_places=3,max_digits=25)
    last_balance = models.DecimalField(decimal_places=3,max_digits=25)
    account = models.ForeignKey(Account)
