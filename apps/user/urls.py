from django.urls import path, include
from django.conf.urls import url
from user.views import SignUp, SignIn, SignInHandle


urlpatterns = [
    url(r'^SignIn$',SignIn,name='SignIn'),
    url(r'^SignUp$', SignUp, name='SignUp'),
    url(r'^SignInHandle$', SignInHandle, name='SignInHandle')
]
