#coding=utf-8
from django.shortcuts import render
from models import *
# Create your views here.


def index(request):
    context = {'head':1,'title':'首页'}
    return render(request,'df_goods/index.html',context)
