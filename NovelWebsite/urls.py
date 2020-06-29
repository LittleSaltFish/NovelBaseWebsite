from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url
from book.views import SearchResult, home

urlpatterns = [
    # path('Search/', SearchResult, name="Search"),
    # url(r'^tinymce/',include('tinymce.urls'))#富文本url
    path('tinymce/', include('tinymce.urls')),  # 富文本url
    path('admin/', admin.site.urls),  # 管理url
    path('Search/', SearchResult, name="Search"),
    path('user/', include(('user.urls','user'))),  # 用户url
    path('book/', include(('book.urls','book'))),  # 书籍url
    path('', include(('chapter.urls','chapter'))),  # 书籍url
    path('', home, name="home"),  # 主页url，放最后降低搜索时间
    # TODO 主页url待优化
]

