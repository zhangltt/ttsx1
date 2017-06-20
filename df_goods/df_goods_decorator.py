#coding=utf-8
from models import *
from django.http import HttpResponse,JsonResponse,HttpRequest
from django.shortcuts import render
from df_carts.models import *
from django.http import HttpResponse,HttpRequest

def user_logn_info(function):


    def function_in(request,*args,**kwargs):
        # 判断用户是否登陆
        if request.session.has_key('user_id'):
            # 获取购物车的商品条数
            cart_nums = CartInfo.objects.filter(user__id=request.session['user_id']).count()
        else:
            cart_nums = 0

        context = function(request,*args,**kwargs)
        print context,'+++'
        # 判断是否为首页
        if context['title'] == '商品列表':
            context['cart_nums']= cart_nums
        return render(request,'df_goods/detail.html',context)

    return function_in

def try_object():
    pass
