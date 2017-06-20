#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from models import *
from pageing import *
from df_carts.models import *
from df_user.decorator import *

# Create your views here.


def index(request):
    # 判断用户是否登陆
    if request.session.has_key('user_id'):
        # 获取购物车的商品条数
        cart_nums = CartInfo.objects.filter(user__id=request.session['user_id']).count()
    else:
        cart_nums = 0

    type_list = TypeInfo.objects.all()
    lists = []
    for type in type_list:
        lists.append({
            'type':type,
            'gclick':type.goodsinfo_set.order_by('-gclick')[0:3],
            'new':type.goodsinfo_set.order_by('-id')[0:4],
        })
    # 需要返回所有商品分类对象的列表
    context = {'head':1,'title':'首页','type_list':lists,'cart_nums':cart_nums}
    return render(request,'df_goods/index.html',context)

# 显示商品列表
def goodslist(request,type_id,pageid=None):
    if request.session.has_key('user_id'):
        # 获取购物车的商品条数
        cart_nums = CartInfo.objects.filter(user__id=request.session['user_id']).count()
    else:
        cart_nums = 0

        # 获取对应商品分类
    type_object = TypeInfo.objects.get(id=int(type_id))

    # 获取新品的前两个
    new2 = type_object.goodsinfo_set.order_by('-id')[0:2]
    # 通过商品查询在排序
    #new22 = GoodsInfo.objects.filter(gtype=type_object.id).order_by('-id')[0:2]
    # 获取排名选项
    response = request.GET.get('opt', '1')

    if response == '1':
        # 获取这个分类下的所有商品按照id倒序
        goods_list = type_object.goodsinfo_set.order_by('-id')
    elif response == '2':
        goods_list = type_object.goodsinfo_set.order_by('gprice')
    elif response == '3':
        goods_list = type_object.goodsinfo_set.order_by('-gclick')

    if pageid == '':
        pageid = 1
        # 创建分页对象,每页显示5个商品,页码数为5
        page = Paging(goods_list, 4,5)
        # 获取总页数
        zy = page.jspages
        # 默认为第一页(没有上一页)
        hasPre = page.has_pre(1)
        # 判断最后一页的范围
        if zy < 5:
            hasNext = page.has_next(zy)
        else:
            hasNext = page.has_next(5)
        # 获取页码列表,默认当前页为第一页
        page_list = page.pageList(1)
        # 获取当前页的商品对象列表
        lgoods =page.current_page(1)

    else:
        pageid = int(pageid)
        # 创建分页对象,每页显示5个商品,页码数为5
        page = Paging(goods_list, 4, 5)
        hasPre = page.has_pre(pageid)
        hasNext = page.has_next(pageid)
        # 获取页码列表,默认当前页为第一页
        page_list = page.pageList(pageid)

        #print page_list,'page_list'
        # 获取当前页的商品对象列表
        lgoods = page.current_page(pageid)
    context = {'head':1,'title':'商品列表','new2':new2,'type_object':type_object,'hasPre': hasPre,
               'hasNext': hasNext, 'page_list': page_list, 'lgoods': lgoods,'pre':pageid-1,'next':pageid+1,
               'cssys':pageid,'opt':response,'cart_nums':cart_nums
               }


    return render(request,'df_goods/list.html',context)

# 显示详情页商品

def goods_detail(request, goodsid):
    # 获取这个商品对应的品类
    type_object = TypeInfo.objects.filter(goodsinfo__id=goodsid)
    # 获取新品的前两个
    new2 = type_object[0].goodsinfo_set.order_by('-id')[0:2]
    # 获取商品对象
    goods_object = GoodsInfo.objects.get(id=goodsid)
    #购物车中的商品条数
    if request.session.has_key('user_id'):
        # 获取购物车的商品条数
        cart_nums = CartInfo.objects.filter(user__id=request.session['user_id']).count()
    else:
        cart_nums = 0
    context={'head':1,'title':'商品列表','new2':new2,'type':type_object[0],"goods":goods_object
             ,'cart_nums':cart_nums}


    return render(request,'df_goods/detail.html',context)


def detail_handle(request):
    nums = request.GET.get('nums',0)
    goodsid = request.GET.get('goodsid',0)
    # 获取购物车对象列表
    object_list = CartInfo.objects.filter(goods__id=int(goodsid))
    # 判断是否有这个商品的对象
    if len(object_list) > 0:
        cart_object = object_list[0]
        cart_object.count += int(nums)
        cart_object.save()
    else:
        # 创建购物车对象,添加商品
        cart_object = CartInfo()
        cart_object.goods = GoodsInfo.objects.get(id=int(goodsid))
        cart_object.count = int(nums)
        cart_object.user = UserInfo.objects.get(id=request.session['user_id'])
        cart_object.save()
    # 获取购物车中这个用户的条数(商品品种的个数)
    cart_nums = CartInfo.objects.filter(user=request.session['user_id']).count()
    return JsonResponse({'count':cart_nums})