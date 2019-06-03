from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from . import views

# 路由
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet, base_name='user')

# 重要的是如下三行
# schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
    path('hello/', views.index),
    path('', views.login),
    path('test/', views.test1, name='test'),

    # path('user/', include(router.urls)),

    #swagger 配置
    path('getJson/', views.ReturnJson.as_view(), name='json'),
    path('addUser/', views.AddUser.as_view(), name='addUser'),
    path('findUsers/', views.FindUsers.as_view(), name='findUsers'),
    path('user/login/', views.userLogin),

    # path('user/docs/', schema_view, name="docs"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # api-auth对应授权登录url

]
