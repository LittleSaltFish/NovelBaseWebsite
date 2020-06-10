# from django.contrib import admin
# from django.urls import path, include
# from django.conf.urls import url
from django.urls import path, include
from user.views import SignUpResult, SignInResult
from django.conf.urls import url


urlpatterns = [
    path('SignUp/', SignUpResult, name="SignUp"),
    path('SignIn/', SignInResult, name="SignIn"),
]
