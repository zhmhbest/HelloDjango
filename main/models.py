from django.db import models


# Create your models here.
class Table(models.Model):
    # varchar(20)
    name = models.CharField(max_length=20)
    # Number
    index = models.IntegerField()
    # date
    date = models.DateField()

