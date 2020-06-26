from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from book.views import SearchResult, home

urlpatterns = [
    # path('Search/', SearchResult, name="Search"),
    # url(r'^tinymce/',include('tinymce.urls'))#富文本url
    path('admin/', admin.site.urls),  # 管理url
    path('user/', include('user.urls')),  # 用户url
    path('star/', include('star.urls')),  # 收藏url
    path('tinymce/', include('tinymce.urls')),  # 富文本url
    path('', include('book.urls')),  # 书籍url
    path('', include('chapter.urls')),  # 书籍url
    path('', home, name="home"),  # 主页url，放最后降低搜索时间
    # TODO 主页url待优化
]

