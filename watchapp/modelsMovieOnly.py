from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True) # movie published

    def __str__(self): #if any object is accessed of Movie class, return movie name
        return self.name

