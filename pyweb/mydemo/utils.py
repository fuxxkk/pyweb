import hashlib
import time
from django.http import QueryDict
from rest_framework.request import Request


def md5_encode(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


def create_uuid():
    return md5_encode(str(time.clock()))


def get_parameter_dic(request, *args, **kwargs):
    if isinstance(request, Request) == False:
        return {}

    query_params = request.query_params
    if isinstance(query_params, QueryDict):
        query_params = query_params.dict()
    result_data = request.data
    if isinstance(result_data, QueryDict):
        result_data = result_data.dict()

    if query_params != {}:
        return query_params
    else:
        return result_data
