from django.db import models

# Create your models here.


class UserInfo(models.Model):
    uname = models.CharField(max_length=30)
    upasswd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=40, default='')
    uiphone = models.CharField(max_length=20, default='')
    usite = models.CharField(max_length=100, default='')
    isDelete = models.BooleanField(default=False)


