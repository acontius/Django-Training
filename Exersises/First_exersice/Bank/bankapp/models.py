from django.db import models
import random

class Bank_acc(models.Model):
    def generate_acc_number(self):
        acc_numbers = ''.join(str(random.randint(0, 9)) for _ in range(8))
        return acc_numbers
    
    acount_number = models.CharField(max_length=20)
    balance = models.CharField(max_length=300)
    type = models.CharField(max_length = 300)
    date = models.DateField()

    def save(self, *args, **kwargs):
        if not self.acount_number:
            self.acount_number = self.generate_acc_number()
        super().save(*args, **kwargs)



    def check_balanced(self):
        return self.balance
    

    def deposit(self , amount):
        self.balance += amount
        return self.balance
    

    def __str__(self) :
        return self.acount_number



class Savings_acc(Bank_acc):
    pass


class Checking_acc(Bank_acc):
    last_transaction = models.DateField()

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else :
             return False

