from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email =  models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    # profile_image = models.ImageField()
    # file = models.FileField()

class Car(models.Model):
    car_name = models.CharField()
    speed = models.IntegerField()

    def __str__(self):
        return f"Car: {self.car_name}, Speed: {self.speed} km/h"