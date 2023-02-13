from django.db import models
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    carmake = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()    
    name = models.CharField(max_length=100)  
    car_type = models.CharField(choices=(('Sedan','Sedan'),
                                         ('SUV', 'SUV'),
                                         ('WAGON', 'WAGON'),
                                         ('COUPE', 'COUPE'),
                                         ('SPORTS', 'SPORTS CAR'),),
                                max_length=100)
    year = models.DateField()
    
    def __str__(self):
        return self.name

