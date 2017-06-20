from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect


def login_check(function):

    def function_in(request,*args,**kwargs):
        if request.session.has_key('user_id'):

            return function(request,*args,**kwargs)
        else:

            return redirect('/user/login/')

    return function_in