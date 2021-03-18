from django.db import models
from django.conf import settings
from django.contrib.auth.hashers import make_password
# from django.contrib.auth.hashers import (
#     PBKDF2PasswordHasher, SHA1PasswordHasher,
# )
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, UserManager


class CustomUser(AbstractUser):
    # username = models.CharField(max_length=40)
    # email = models.CharField(max_length=35, unique=True)
    # password = models.CharField(max_length=20)
    # make_password(password)
    phnum = models.CharField(max_length=13)
    location = models.CharField(max_length=40)
    zipcode = models.CharField(max_length=40)
    category = models.CharField(max_length=15, null=True)
    charges = models.CharField(max_length=4, default='NULL')
    image = models.ImageField(upload_to='pics', default='NULL')
    bio = models.CharField(max_length=400, default='NULL')
    # REQUIRED_FIELD = ['username']
    review = models.FloatField(default=0)


class Order_table(models.Model):
    orderid = models.CharField(max_length=14)
    email = models.EmailField()
    phnum = models.CharField(max_length=13)
    fullname = models.CharField(max_length=20)
    location = models.CharField(max_length=150)
    category = models.CharField(max_length=12, default='NULL')
    service_provider = models.EmailField(default = 'NULL')

class Image_table(models.Model):
    uid = models.CharField(max_length=10000)
    description = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics', default='NULL')


# class User(models.Model):

#     username = models.CharField(max_length=40, unique=True)
#     email = models.CharField(max_length=35, unique=True, primary_key=True)
#     password = models.CharField(max_length=20)
#     # make_password(password)
#     phnum = models.CharField(max_length=12)
