from django.shortcuts import render, redirect
from user.models import User
import re
from django.urls import reverse

# Create your views here.

def SignUp(request):
    '''显示登录界面'''
    return render(request, 'SignUp.html')


def SignIn(request):
    '''显示注册界面'''
    return render(request, 'SignIn.html')

def SignInHandle(request):
    '''进行注册处理'''
    user_name = request.POST.get('user_name')
    user_pwd = request.POST.get('user_pwd')
    user_cpwd = request.POST.get('user_cpwd')
    user_email = request.POST.get('user_email')
    allow = request.POST.get('allow')

    # 数据完整性校验
    if not all([user_name, user_pwd, user_cpwd, user_email]):
        return render(request, 'SignIn.html', {'errmsg': '数据不完整'})
    # 邮箱合法性校验
    if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', user_email):
        return render(request, 'SignIn.html', {'errmsg': '邮箱不合法'})
    # 确认密码校验
    if user_pwd != user_cpwd:
        return render(request, 'SignIn.html', {'errmsg': '密码不一致'})
    # 协议确认
    if allow != 'on':
        return render(request, 'SignIn.html', {'errmsg': '未同意协议'})

    # 非django式写法
    # user = User()
    # user.username=user_name
    # user.password=user_pwd
    # user.email=user_email
    # user.save()

    # TODO raw式写法

    # django味注册
    User.objects.create_user(user_name, user_email, user_pwd)

    # 返回应答,到首页
    return redirect(reverse('home'))
