#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from models import *
from hashlib import sha1
# Create your views here.

def register(request):
    # 判断是否是ajax请求
    a = request.is_ajax()
    print a
    if request.is_ajax():
        # 接收GET请求,判断用户名,邮箱是否存在,存在返回1,否则可以写入数据库
        result = request.GET

        rname = result.get('name', 0)
       # print rname
        remail = result.get('email', 0)
        dbname = UserInfo.objects.filter(uname=rname)
        dbemail = UserInfo.objects.filter(uemail=remail)
        #count = UserInfo.objects.filter(uname=uname).count()
        #print dbname
        print dbemail,1


        if len(dbname) > 0:
            #print dbname[0].uname
            return JsonResponse({'name':rname})
            #rname=0
        else:
            rname = 0
            if len(dbemail) > 0:
                print dbemail, 2
                print '======'
                return JsonResponse({'email': remail})
            else:
                print dbemail, 3
                remail = 0
                context = {'title': '注册', 'name': rname, 'email': remail}
                #return JsonResponse({'email': remail})

                return JsonResponse(context)


    else:

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
    pass


def center_info(request):
    pass


def center_order(request):
    pass


def center_siter(request):
    pass