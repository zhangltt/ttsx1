#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from models import *
from hashlib import sha1
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



def login(request):
    context = {'title': '登陆'}
    return render(request, 'df_user/login.html', context)


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
            reponse = redirect('/user/register/')
            if juser == '1':
                reponse.set_cookie('user_name', ruser)
            else:
                reponse.delete_cookie('user_name')
            request.session['user_id'] = dbuser[0].id
            se = request.session.get('user_id')
            print se,'se'
            return reponse
    else:
        cuser = 0
        if len(dbpasswd) > 0:
            cpasswd = 1
        else:
            cpasswd = 0
        del request.session['user_id']
        se = request.session.get('user_id')
        print se, 'se'
        context = {'cuser': cuser, 'cpasswd': cpasswd, }
        return render(request, 'df_user/register.html', context)








def center_info(request):
    pass


def center_order(request):
    pass


def center_siter(request):
    pass