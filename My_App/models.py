from django.db import models

# Create your models here.

class Emp(models.Model):
    eno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=100)