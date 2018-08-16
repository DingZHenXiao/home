from django.db import models

# Create your models here.
class Users(models.Model):
    """docstring for ClassName"""
    uname = models.CharField(max_length=30)
    upwd = models.CharField(max_length=30)
    uage = models.IntegerField()
    uemail = models.EmailField()
    def to_dic(self):
        dic = {
            "uname" : self.uname,
            "upwd" : self.upwd,
            "uage" : self.uage,
            "uemail" : self.uemail,
            "id": self.id,
        }
        return dic 
        