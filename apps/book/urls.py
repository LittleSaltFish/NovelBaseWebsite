from django.urls import path, include,reverse
from book.views import BookDetailView, SearchResult, home
from django.conf.urls import url

urlpatterns = [
    # url(r'^Search/(?P<SearchInput>\d+)', SearchResult, name="Search"),
    # path('Search/', SearchResult, name="Search"),
    path('<str:book_id>/', BookDetailView.as_view(),name='BookDetail')
]
