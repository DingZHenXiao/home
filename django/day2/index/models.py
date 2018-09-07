from django.db import models

# Create your models here.
class tday2(models.Model):
    """docstring for tday2"""
    name=models.CharField(max_length=30)
    age=models.IntegerField()

class Users(models.Model):
    """docstring for Users"""
    uname=models.CharField(max_length=20)
    upwd=models.CharField(max_length=20)
    uphone=models.CharField(max_length=11)
    uemile=models.EmailField()
    isActive=models.BooleanField(default=True)

class GoogsType(models.Model):
    title= models.CharField(max_length=20)
    picture= models.ImageField(upload_to="static/upload/goodstype")
    desc=models.TextField()

class Googs(models.Model):
    """docstring for Googs"""
    title=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    spec=models.CharField(max_length=20)
    picture=models.ImageField(upload_to="static/upload/goods")
    isActive=models.BooleanField(default=True)