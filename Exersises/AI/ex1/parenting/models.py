# Angolacing the data bass just for fun 

from django.db import models

class Parent(models.Model):
    name: str = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Child(models.Model):
    parent: str = models.ForeignKey(Parent,on_delete=models.CASCADE)
    name: str   = models.CharField(max_length=70)

    def __str__(self):
        return self.name