from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse("hello world")


def login(request):
    return render(request, 'pages/login.html')
