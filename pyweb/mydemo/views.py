from datetime import datetime
import coreapi

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from mydemo.models import User
from rest_framework.schemas import AutoSchema
from rest_framework.views import APIView

from mydemo.utils import get_parameter_dic
import logging

logger = logging.getLogger('django')
from mydemo import utils


def index(request):
    return HttpResponse("hello world")


def login(request):
    return render(request, 'pages/login.html')


def test1(request):
    users = User.objects.filter(username__contains='admin')
    print(users)
    return HttpResponse(users)


class ReturnJson(APIView):
    schema = AutoSchema(manual_fields=[
        coreapi.Field(name="token", required=True, location="query", description="用户名"),
    ])

    def get(self, request, *args, **kwargs):
        token = request.GET['token']
        print('token', token)
        return HttpResponse("Hello world!!!!!!!!++++++中文测试:" + token)


# 添加用户
class AddUser(APIView):
    # coreapi_fields = (
    #     DocParam(name="username"),
    #    # DocParam(name="pwd"),
    # )

    schema = AutoSchema(manual_fields=[
        coreapi.Field(name="name", required=True, location="query", description="用户名"),
        coreapi.Field(name="pwd", required=True, location="query", description="密码"),
    ])

    def post(self, request, *args, **kwargs):
        data = get_parameter_dic(request)
        name = data['name']
        pwd = data['pwd']

        user = User()
        user.id = utils.create_uuid()
        user.username = name
        user.password = utils.md5_encode(pwd)
        user.create_date = datetime.now()
        user.modify_date = datetime.now()
        save = user.save()

        print(type(save))
        return HttpResponse("user saved!  :" + name + " , " + pwd)


class FindUsers(APIView):
    schema = AutoSchema(manual_fields=[
        coreapi.Field(name="username", required=True, location="query", description="用户名"),
    ])

    def get(self, request, *args, **kwargs):
        username = request.GET['username']
        user_list = User.objects.filter(username__contains=username)
        print(user_list)
        users = utils.toJson(user_list)
        return HttpResponse(users)


def userLogin(request):
    # schema = AutoSchema(manual_fields=[
    #     coreapi.Field(name="username", required=True, location="query", description="用户名"),
    #     coreapi.Field(name="password", required=True, location="query", description="密码"),
    # ])
    #params = get_parameter_dic(request)
    username = request.POST['username']
    password = request.POST['password']
    count = User.objects.filter(username=username, password=password).count()
    if count > 0:
        context = {'username': username, 'password': password}
        return render(request, 'pages/login.html', context)
