from django.db import models

# Create your models here.

class Superuser(models.Model):
    id=models.AutoField(unique=True, primary_key=True)
    username=models.CharField(max_length=30)
    password=models.TextField(max_length=50)
    email=models.EmailField(unique=True)

    