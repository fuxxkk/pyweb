from django.db import models


# Create your models here.
class User(models.Model):
    # id
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    # 用户名
    username = models.CharField(max_length=225, unique=True, null=False)
    # 密码
    password = models.CharField(max_length=225)

    create_date = models.DateField(null=True)

    modify_date = models.DateField()
