from django.db import models

# Create your models here.
class Employee(models.Model):
    eno= models.IntegerField()

    ename= models.CharField(max_length=22)
    esal=models.FloatField()
    eadd=models.CharField(max_length=200)

    venu = models.Manager()
