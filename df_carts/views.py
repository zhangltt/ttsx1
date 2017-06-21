#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from models import *
from df_user.decorator import *
# Create your views here.


@login_check
def cart(request):
    # 获取购物车中的商品对像
    goods_object = CartInfo.objects.filter(user__id=request.session['user_id'])
    # 获取购物车的条数
    cart_nums = goods_object.count()
    context = {'head':1,'title':'购物车','cart_nums':cart_nums,'goods_object':goods_object}

    return render(request,'df_cart/cart.html',context)

def cart_handle(request):
    rget = request.GET
    cart_id = rget.get('cart_id')
    status = rget.get('status')
    counts = rget.get('count')
    print cart_id
    print status
    print counts

    # 获取购物车中对应商品的对象
    try:
        goods = CartInfo.objects.get(id=int(cart_id))
    except:
        pass
    # 根据穿回来的状态码进行操作

    if status == 'add':
        goods.count+=int(counts)
        goods.save()
    if status == 'minus':
        goods.count-=int(counts)
        goods.save()
    if status == 'd':
        goods.delete()
    cart_count = CartInfo.objects.filter(user=request.session['user_id']).count()

    context = {'cart_count':cart_count}
    return JsonResponse(context)