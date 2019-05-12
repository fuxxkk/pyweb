from django.db import models


# Create your models here.
class User(models.Model):
    # id
    id = models.IntegerField(primary_key=True, unique=True)
    # 用户名
    username = models.CharField(max_length=225)
    # 密码
    password = models.CharField(max_length=225)

    create_date = models.DateField()
