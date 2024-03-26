#To save any thing we want in the database of the current app
from django.db import models

class Question(models.Model):
    text = models.CharField(max_length = 300)
    date = models.DateField()


    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question , on_delete=models.CASCADE )
    Choice = models.CharField(max_length = 300)
    votes = models.IntegerField(default = 0)


    def __str__(self):
        return self.Choice