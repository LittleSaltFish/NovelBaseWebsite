from django.urls import path, include
from django.conf.urls import url
from user.views import SignUpView, SignInView


urlpatterns = [
    url(r'^SignIn$', SignInView.as_view(), name='SignIn'),
    url(r'^SignUp$', SignUpView.as_view(), name='SignUp'),
]
