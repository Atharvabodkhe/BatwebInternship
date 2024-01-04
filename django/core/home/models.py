from django.db import models

# Create your models here.
class Student(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    phone = models.IntegerField(max_length = 10)
