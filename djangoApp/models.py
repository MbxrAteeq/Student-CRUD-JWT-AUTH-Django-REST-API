from django.db import models

# Create your models here.

class Student(models.Model):

    # id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=45)
    grades = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    phoneNumber = models.CharField(max_length=13)
