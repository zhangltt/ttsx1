#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from models import *
from pageing import *
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
   # print lists
    # 需要返回所有商品分类对象的列表
    context = {'head':1,'title':'首页','type_list':lists}
    return render(request,'df_goods/index.html',context)

# 显示商品列表
def goodslist(request,type_id,pageid=None):
    #pageid = int(request.GET.get('pageid',0))
        # 获取对应商品分类
    type_object = TypeInfo.objects.get(id=int(type_id))


    # 获取新品的前两个
    new2 = type_object.goodsinfo_set.order_by('-id')[0:2]
    # 通过商品查询在排序
    #new22 = GoodsInfo.objects.filter(gtype=type_object.id).order_by('-id')[0:2]

    response = request.GET.get('opt', '1')

    if response == '1':
        # 获取这个分类下的所有商品按照id倒序
        goods_list = type_object.goodsinfo_set.order_by('-id')
    elif response == '2':
        goods_list = type_object.goodsinfo_set.order_by('gprice')
    elif response == '3':
        goods_list = type_object.goodsinfo_set.order_by('-gclick')

    if pageid == '':
        # 创建分页对象,每页显示5个商品,页码数为5
        page = Paging(goods_list, 10,5)
        # 获取总页数
        zy = page.jspages()
        # 默认为第一页(没有上一页)
        hasPre = page.has_pre(1)
        # 判断最后一页的范围
        if zy < 5:
            hasNext = page.has_next(zy)
        else:
            hasNext = page.has_next(5)

        # 获取页码列表,默认当前页为第一页
        page_list = page.d_pages(1)

        # 获取当前页的商品对象列表
        lgoods =page.current_page(1)
        print pageid,'pageid'
        context = {'head':1,'title':'商品列表','new2':new2,'type_object':type_object,
                   'hasPre':hasPre,'hasNext':hasNext,'page_list':page_list,'lgoods':lgoods,
                   'cssys':1,'opt':response
                   }

       # return render(request,'df_goods/list.html',context)

    else:

        pageid = int(pageid)
        # 查询所有的商品
        #goods_list = GoodsInfo.objects.filter(gtype__id=int(1))

        # 创建分页对象,每页显示5个商品,页码数为5
        page = Paging(goods_list, 10, 5)
        # 获取总页数
        zy = page.jspages()

        hasPre = page.has_pre(pageid)
        # 判断最后一页的范围
        # if zy < 5:
        #     hasNext = page.has_next(zy)
        # else:
        #     hasNext = page.has_next(5)

        hasNext = page.has_next(pageid)
        # 获取页码列表,默认当前页为第一页
        page_list = page.d_pages(pageid)
        #print page_list,'page_list'
        # 获取当前页的商品对象列表
        lgoods = page.current_page(pageid)
        context = {'head':1,'title':'商品列表','new2':new2,'type_object':type_object,'hasPre': hasPre,
                   'hasNext': hasNext, 'page_list': page_list, 'lgoods': lgoods,'pre':pageid-1,'next':pageid+1,
                   'cssys':pageid,'opt':response
                   }
    print pageid
    return render(request,'df_goods/list.html',context)
   # return HttpResponse('ok')
        #return JsonResponse({})

def goods_order(request):
    response = request.GET.get('opt',0)
    def function_in():
        pass
    pass