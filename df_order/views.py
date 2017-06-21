# coding=utf-8
from django.shortcuts import render
from models import *

# Create your views here.

def order(request):
    post = request.POST
    # 获取总计
    zj = post.get('zj')
    # 获取购物车id列表
    cart_id = post.getlist('cart_id')

    context = {'zj':zj}
    return render(request,'df_order/place_order.html')
