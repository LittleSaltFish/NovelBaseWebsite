from django.urls import path, include
from django.conf.urls import url
from user.views import SignUpView, SignInView, LogOutView,UserMainPage


urlpatterns = [
    # url(r'^SignIn$', SignInView.as_view(), name='SignIn'),
    # url(r'^SignUp$', SignUpView.as_view(), name='SignUp'),
    # url(r'^LogOut$', LogOutView.as_view(), name='LogOut'),
    path('SignIn', SignInView.as_view(), name='SignIn'),
    path('SignUp', SignUpView.as_view(), name='SignUp'),
    path('LogOut', LogOutView.as_view(), name='LogOut'),
    path('UserMainPage/<str:username>/',UserMainPage.as_view(),name='UserMainPage')
]
