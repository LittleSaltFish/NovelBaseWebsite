from django.shortcuts import render, redirect
from user.models import User
import re
from django.urls import reverse
from django.db import connection
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class LogOutView(View):
    '''退出登录'''
    def get(self,request):
        #清除用户session信息
        logout(request)
        #返回首页
        return redirect(reverse('home'))

class SignInView(View):
    '''注册视图类'''

    def get(self, request):
        '''当请求方式为get时显示界面'''
        return render(request, 'SignIn.html')

    def post(self, request):
        '''当请求方式为post时进行注册处理'''
        user_name = request.POST.get('user_name')
        user_pwd = request.POST.get('user_pwd')
        user_cpwd = request.POST.get('user_cpwd')
        user_email = request.POST.get('user_email')
        allow = request.POST.get('allow')

        cursor = connection.cursor()
        cursor.execute(
            "select * from user where username =\" " + str(user_name)+"\"")
        # NOTE 此处要打引号
        duplicate = True if len(cursor.fetchall()) != 0 else False

        # 用户名重复检验
        if duplicate:
            return render(request, 'SignIn.html', {'errmsg': '用户名重复'})
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
        # NOTE 这样写注册完还得二次登录，用户体验不好
        # return redirect(reverse('home'))
        
        # 直接登录，提升用户体验
        # django内置校验
        user = authenticate(username=user_name, password=user_pwd)
        if user is not None:
            # 账号密码正确
            # 记录登陆状态
            login(request, user)

            #跳转首页
            return redirect(reverse('home'))
        else:
            return render(request, 'SignUp.html', {'errmsg': '用户名or密码错误'})

class UserMainPage(View):
    '''用户主页'''
    def get(self,request):
        return render(request,'user.html')


class SignUpView(View):
    '''显示登录界面'''

    def get(self, request):
        return render(request, 'SignUp.html')

    def post(self, request):
        user_name = request.POST.get('user_name')
        user_pwd = request.POST.get('user_pwd')

        if not all([user_name, user_pwd]):
            return render(request, 'SignUp.html', {'errmsg': '数据不完整'})

        #django内置校验        
        user = authenticate(username=user_name, password=user_pwd)
        if user is not None:
            # 账号密码正确
            # 记录登陆状态
            login(request,user)
            
            #跳转首页
            return redirect(reverse('home'))
        else:
            return render(request, 'SignUp.html', {'errmsg': '用户名or密码错误'})
