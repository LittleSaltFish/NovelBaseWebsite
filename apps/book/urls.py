from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name="home"),
    path('Search/', views.SearchResult, name="Search"),
    # url(r'^BookDetail/(?P<book_id>\d+)', views.

]
