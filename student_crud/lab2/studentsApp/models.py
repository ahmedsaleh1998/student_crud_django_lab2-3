from pickle import TRUE
from django.db import models

# Create your models here.

class student(models.Model):
    id=models.AutoField(unique=True, primary_key=True)
    name=models.CharField(max_length=30)
    password=models.TextField(max_length=50 ,default='admin')
    email=models.EmailField(unique=True)

