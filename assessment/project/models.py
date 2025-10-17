from django.db import models


class Signup(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=15)
    password = models.CharField(max_length=8)  

    # def __str__(self):
    #     return self.fullname




class Login(models.Model):
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15)
    password = models.CharField(max_length=8)  

    # def __str__(self):
    #     return self.email
