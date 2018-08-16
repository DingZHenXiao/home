from django.db import models

# Create your models here.
class Users(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=20)
    uemail = models.CharField(max_length=30)
    uage = models.IntegerField()
        