from django.db import models

# Create your models here.
class Signup(models.Model):
    fullname = models.TextField()
    email = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=10)
    password = models.CharField(max_length=8)
    confirmpassword = models.CharField(max_length=8)





class login(models.Model):
    email = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=10)
    password = models.CharField(max_length=8)