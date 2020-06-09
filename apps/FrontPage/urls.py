from django.urls import path,include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('',views.home,name="home"),
    path('search/', views.SearchResult, name="search"),
]
