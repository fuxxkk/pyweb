import time
from datetime import datetime

from django.test import TestCase

# Create your tests here.
from mydemo.models import User

class Test1(TestCase):

    def save(self):
        u1 = User()
        u1.id = 1
        u1.username = "admdin"
        u1.password = "1234"
        u1.create_date = datetime.now()
        u1.modify_date = datetime.now()
        u1.save()


t1 = Test1()
t1.save()
