from django.db import models


# Create your models here.
class User(models.Model):
    # id
    id = models.CharField(max_length=225, primary_key=True, unique=True, null=False)
    # 用户名
    username = models.CharField(max_length=225, unique=True, null=False)
    # 密码
    password = models.CharField(max_length=225)

    create_date = models.DateTimeField(null=True)

    modify_date = models.DateTimeField()

    def __str__(self):
        return '{id :' + self.id + ",username:" + self.username + ",password:" + self.password +\
               ",create_date:" + str(self.create_date) + ",modify_date:" + str(self.modify_date)+"}"
