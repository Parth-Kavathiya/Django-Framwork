from django.db import models

# Create your models here.
class newUser(models.Model):
    FirstName = models.CharField(max_length=25)
    LastName = models.CharField(max_length=25)
    Email = models.EmailField()
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=30)
    Password = models.CharField(max_length=25)
    Mobile = models.BigIntegerField()
    