from django.db import models

# Create your models here.
class user(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.BigIntegerField()
    city=models.TextField()
    state=models.TextField()
    mobile=models.BigIntegerField()