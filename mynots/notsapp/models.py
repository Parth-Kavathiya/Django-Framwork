from django.db import models

# Create your models here.
class newuser(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Email = models.EmailField()
    Password = models.CharField(max_length=30)
    Phone = models.BigIntegerField()