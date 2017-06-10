#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from models import *
from hashlib import sha1
from decorator import *
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

# Create your views here.

def register(request):
    # 判断是否是ajax请求
    if request.is_ajax():
        # 接收GET请求,判断用户名,邮箱是否存在,存在返回1,否则可以写入数据库
        result = request.GET
        rname = result.get('name', 0)
        remail = result.get('email', 0)
        dbname = UserInfo.objects.filter(uname=rname)
        dbemail = UserInfo.objects.filter(uemail=remail)
        if len(dbname) > 0:
            return JsonResponse({'name':rname})
        else:
            rname = 0
            if len(dbemail) > 0:
                return JsonResponse({'email': remail})
            else:
                print dbemail, 3
                remail = 0
                context = {'title': '注册', 'name': rname, 'email': remail}
                return JsonResponse(context)
    else:
        # post请求接收
        presult = request.POST
        puser = presult.get('user_name', 0)
        ppasswd = presult.get('pwd', 0)
        pcpasswd = presult.get('cpwd', 0)
        pemail = presult.get('email', 0)
        pallow = presult.get('allow', 0)
        dbuser = UserInfo.objects.filter(uname=puser)
        dbpemail = UserInfo.objects.filter(uemail=pemail)
        if puser != dbuser and ppasswd == pcpasswd and pallow == '1' and pemail != dbpemail:
            s1 = sha1()
            s1.update(ppasswd)
            passwd_sha1 = s1.hexdigest()
            user_name = UserInfo()
            user_name.uname = puser
            user_name.upasswd = passwd_sha1
            user_name.uemail = pemail
            user_name.save()
            return render(request, 'df_user/register.html')
        return render(request, 'df_user/register.html',{'title':'注册'})

# 显示登陆
def login(request):
    context = {'title': '登陆'}
    return render(request, 'df_user/login.html', context)



# 处理登陆
def login_handler(request):
    # 创建post对象
    post_object = request.POST
    # 接收用户名,密码和记住用户的值(等于'1'表示勾选)
    ruser = post_object.get('username')
    rpasswd = post_object.get('pwd')
    juser = post_object.get('juser')
    # 获取数据库中的用户信息
    dbuser = UserInfo.objects.filter(uname=ruser)
    # 获取的密码加密
    s1 = sha1()
    s1.update(rpasswd)
    rpasswd_sha1 = s1.hexdigest()
    dbpasswd = UserInfo.objects.filter(upasswd=rpasswd_sha1)
    # 判断输入的信息是否与数据库中的相同,相同返回1,不同返回0
    if len(dbuser)>0:
        if dbuser[0].uname == ruser:
            cuser = 1
        else:
            cuser = 0
        # 判断密码
        if len(dbpasswd) > 0:
            if rpasswd_sha1 == dbpasswd[0].upasswd:
                cpasswd = 1
            else:
                cpasswd = 0

            # 判断是否记住账户,记住写入cookie
            reponse = redirect('/user/center_info/')
            if juser == '1':
                reponse.set_cookie('user_name', ruser)
            else:
                reponse.delete_cookie('user_name')
            # 记录用户登陆的id,方便以后的查询
            request.session['user_id'] = dbuser[0].id
            request.session['user_name'] = dbuser[0].uname
            #se = request.session.get('user_id')
           # print se,'se'
            return reponse
    else:
        cuser = 0
        if len(dbpasswd) > 0:
            cpasswd = 1
        else:
            cpasswd = 0
        # 删除数据库中存储的用户登陆id
        del request.session['user_id']
        del request.session['user_name']
        #se = request.session.get('user_id')
        #print se, 'se'
        context = {'cuser': cuser, 'cpasswd': cpasswd, }
        return render(request, 'df_user/register.html', context)

# 退出
def logout(request):
    request.session.flush()
    return redirect('/user/login/')



# 显示用户信息
@login_check
def center_info(request):
    user_name = request.session.get('user_name')
    user_object = UserInfo.objects.filter(id=request.session.get('user_id'))
    user_phone = user_object[0].uiphone
    user_site = user_object[0].usite
    # 上下问参数 用户名,联系方式,联系地址
    context = {'title':'用户中心','ys':1,'user_name': user_name, 'user_phone': user_phone, 'user_site': user_site}
    return render(request,'df_user/user_center_info.html',context)

# 处理用户信息-最近浏览
def info_handler(request):
    # 最近浏览

    return JsonResponse({})


# 显示用户订单
def center_order(request):
    context = {'title': '用户中心', 'ys':2}
    return render(request, 'df_user/user_center_order.html', context)

# 显示用户地址
def center_siter(request):

    user_object = UserInfo.objects.get(id=request.session.get('user_id'))
    name = user_object.sjr
    siter = user_object.usite
    phone = user_object.uiphone
    yb = user_object.yubian
    siter_str = siter + '  邮编:' + yb + ' ( 收件人:' + name + ') ' + '联系方式:' + phone
    context = {'title': '用户中心', 'ys':3,'siter_str':siter_str}

    return render(request, 'df_user/user_center_site.html', context)

def siter_handler(request):
    # 获取信息
    request_object = request.POST
    name = request_object.get('sname','')
    siter = request_object.get('ssiter','')
    phone = request_object.get('sphone','')
    yb = request_object.get('syb','')
    user_object = UserInfo.objects.get(id=request.session.get('user_id'))
    print user_object
    user_object.sjr = name
    user_object.uiphone = phone
    user_object.usite = siter
    user_object.yubian = yb
    user_object.save()
    # 拼接收货地址
    siter_str = siter+'  邮编:'+yb+' ( 收件人:'+name+') '+'联系方式:'+phone
    context = {'siter_str':siter_str,'ys':3}
    return render(request,'df_user/user_center_site.html',context)