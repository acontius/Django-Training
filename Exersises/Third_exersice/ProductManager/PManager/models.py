from django.db import models
from django.utils import timezone

class Clients(models.Model):
    name = models.CharField(max_length = 300)
    company = models.CharField(max_length = 300)


class ClientsOrders(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    each_date = models.DateField()
    OrderNumber = models.CharField(unique = True,max_length = 11)


    def save(self, *args, **kwargs):
        if not self.OrderNumber:
            timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
            self.OrderNumber = f"{timestamp}-{self.client.id}"
        super().save(*args, **kwargs)




class Manufacture(models.Model):
    name = models.CharField(max_length = 30)
    location = models.CharField(max_length = 30)



class Product(models.Model):
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE)
    CostPerItem = models.DecimalField(max_digits = 5 , decimal_places = 2)
    ProName = models.CharField(max_length=50)



class Factor(models.Model):
    client_order = models.ManyToManyField(ClientsOrders)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)    
    client = models.ForeignKey(Clients, on_delete = models.CASCADE)
    manufacture = models.ForeignKey(Manufacture,on_delete = models.CASCADE)


    def __str__(self):
        return f"Client: {self.client.name}, Product: {self.product.ProName}, Oreders : {self.client_order} , Manufacture : {self.manufacture.name}"