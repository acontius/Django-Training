from django.db import models
import uuid
from django.urls import reverse



class Type(models.Model):
    type = models.CharField(max_length=100,null=True,blank=True,help_text="Car's Type (e.g. SUV)")
    manufacture = models.ForeignKey('Manufacture', blank=True,null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    


# manufacturerId = models.UUIDField(unique=True,default=uuid.uuid4) 
class Manufacture(models.Model):
    name     =  models.CharField(max_length=50)
    location =  models.CharField(max_length=300,null=True,help_text="where are the manufature's branchs")
    brand    =  models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})



class Fuel(models.Model):
    FUEL_TYPES = (
        ('p', 'Petrol'),
        ('g', 'Gas'),
        ('e', 'Electronic'),
    )
    fuel = models.CharField(max_length=100,choices=FUEL_TYPES,default='p',help_text="What this car need to work")

    def __str__(self):
        return self.fuel
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})

class Car(models.Model):
    carId        = models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4,help_text="ID of the car")
    carName      = models.CharField(max_length = 100)
    manufacture  = models.ForeignKey(Manufacture,null=True,on_delete=models.SET_NULL)
    carType      = models.ForeignKey(Type,null=True,blank=True,on_delete=models.SET_NULL)
    fuel         = models.ForeignKey(Fuel,null=True,blank=True,on_delete=models.SET_NULL)
    date         = models.DateField(help_text="The date of manufacture of this car")
    capacity     = models.IntegerField(help_text="The number of this car's capacity")
    distance     = models.IntegerField(help_text="Distance that this car travled")
    inventory    = models.IntegerField()


    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.carName