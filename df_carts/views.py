#coding=utf-8
from django.shortcuts import render
from models import *
from df_user.decorator import *
# Create your views here.


@login_check
def cart(request):
    print '+++++'
    # 获取购物车中的商品对像
    goods_object = CartInfo.objects.filter(user__id=request.session['user_id'])
    # 获取购物车的条数
    cart_nums = goods_object.count()


    context = {'head':1,'cart_nums':cart_nums,'goods_object':goods_object}

    return render(request,'df_cart/cart.html',context)
