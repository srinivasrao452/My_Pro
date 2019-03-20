from django.db import models

# Create your models here.

class Emp(models.Model):
    eno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=100)

    esal = models.DecimalField(max_digits=10,decimal_places=2)
    