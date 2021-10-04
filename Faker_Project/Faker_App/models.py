
from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=100)
    city = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    salary = models.IntegerField()

    def __str__(self):
        return self.username


