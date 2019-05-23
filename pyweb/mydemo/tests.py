import time
import uuid
from datetime import datetime

from django.test import TestCase

import hashlib

# Create your tests here.
from mydemo import utils
from mydemo.models import User


class Test1(TestCase):

    def save(self):
        u1 = User()
        u1.id = utils.create_uuid()
        u1.username = "admdin5"
        u1.password = utils.md5_encode("1234")
        u1.create_date = datetime.now()
        u1.modify_date = datetime.now()
        u1.save()


# t1 = Test1()
# t1.save()

# batch insert
def batch_insert():
    users = []
    for i in range(1, 1000):
        u1 = User()
        u1.id = utils.create_uuid()
        u1.username = "admin" + str(i)
        u1.password = utils.md5_encode("1234")
        u1.create_date = datetime.now()
        u1.modify_date = datetime.now()
        users.append(u1)

    User.objects.bulk_create(users)

def select_like():
    users = User.objects.filter(username__contains='admin')
    print(users)

select_like()
#batch_insert()
