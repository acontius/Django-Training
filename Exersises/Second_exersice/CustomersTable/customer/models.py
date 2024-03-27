from django.db import models
from django.core.validators import MaxValueValidator

class Customers(models.Model):
    id = models.PositiveIntegerField(primary_key = True ,default = "" , validators = [MaxValueValidator(99999999999)])
    Name = models.CharField(max_length = 20 , default = "")
    Age = models.IntegerField(blank = True)

    Address = models.CharField(max_length = 25,default = None)
    Salary = models.DecimalField(max_digits = 18,decimal_places = 2)


    def __str__(self):
        return self.Name
    
    
