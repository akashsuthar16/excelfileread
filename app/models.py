from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=255,default='name')
    contect = models.BigIntegerField(default=123456789)
    email = models.EmailField(unique=True,default='email@gmail.com')
    Hobby = models.CharField(max_length=255,default='hobby')

class us_file(models.Model):
    titel = models.CharField(max_length=255,default="slogan")
    o_file = models.FileField(upload_to="file/",default=".xls")

