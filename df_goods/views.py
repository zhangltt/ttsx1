#coding=utf-8
from django.shortcuts import render
from models import *
# Create your views here.


def index(request):
   # goodType = TypeInfo()

    type_list = TypeInfo.objects.all()
    lists = []
    for type in type_list:
        lists.append({
            'type':type,
            'gclick':type.goodsinfo_set.order_by('-gclick')[0:3],
            'new':type.goodsinfo_set.order_by('-id')[0:4],
        })
    print lists
    # 需要返回所有商品分类对象的列表
    context = {'head':1,'title':'首页','type_list':lists}
    return render(request,'df_goods/index.html',context)
