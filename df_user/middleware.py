from django.http import HttpRequest,HttpResponse
from django.middleware.csrf import CsrfViewMiddleware

class url():
    def process_response(self,request, response):
        url_list=[
            '/user/login/',
            '/user/login_handler/',
            '/user/logout/',
            '/user/register/',
        ]
        if not request.is_ajax() and request.path not in url_list:
            response.set_cookie('url',request.get_full_path())
        return response
