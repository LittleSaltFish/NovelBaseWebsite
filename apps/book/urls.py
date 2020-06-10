from django.urls import path, include,reverse
from book.views import BookDetailView, SearchResult, home
from django.conf.urls import url

urlpatterns = [
    path('', home, name="home"),
    path('Search/', SearchResult, name="Search"),
    url(r'^BookDetail/(?P<book_id>\d+)', BookDetailView.as_view(),name='BookDetail')

]
