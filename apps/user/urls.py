# from django.contrib import admin
# from django.urls import path, include
# from django.conf.urls import url
from django.urls import path, include
from . import views
from django.conf.urls import url


urlpatterns = [
    path('SignUp/', views.SignUpResult, name="SignUp"),
    path('SignIn/', views.SignInResult, name="SignIn"),
]
