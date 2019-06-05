from django.shortcuts import redirect, render
from django.utils.deprecation import MiddlewareMixin

from pyweb.settings import UNFILTER


class LoginMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        print("request path: ", request.path)
        if request.path not in UNFILTER:
            if request.session.get('user') is None:
                return render(request, 'pages/login.html')
