from django.db import models
from django.utils import timezone
import random 

class BankAccount(models.Model):
    Balance          = models.IntegerField()
    accountNumber    = models.CharField(max_length = 11)
    type             = models.CharField(max_length=30)
    dateCreate       = models.DateField()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.acountNumberList = []

    def generate(self):
        accNum = ''
        for _ in range(10):
            accNum += str(random.randint(0,10))
        accNum = int(accNum)
        if accNum not in self.acountNumberList:
            self.acountNumberList.append(accNum)
        return accNum

    def checkBAlance(self):
        return f"Balance : {self.Balance}"
    
    #adding another amount of Money
    def deposit(self,amount):
        self.Balance += amount
        return self.Balance


    def __str__(self):
        return f"account Number : {self.accountNumber} ,  type : {self.type}"

class SavaingAccount(BankAccount):
    pass


class CheckingAccount(BankAccount):
    withdrawal = 0
    lastTransaction = models.DateField()
    def withdrawal (self , withdrawal):
        if withdrawal == 1:
            self.Balance = 0
            self.type = "No Input"
            withdrawal = 0
