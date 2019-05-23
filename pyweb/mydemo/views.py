from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from mydemo.models import User


def index(request):
    return HttpResponse("hello world")


def login(request):
    return render(request, 'pages/login.html')


def test1(request):
    users = User.objects.filter(username__contains='admin')
    print(users)
    return HttpResponse(users)
