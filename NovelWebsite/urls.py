from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),  # 管理url
    # url(r'^tinymce/',include('tinymce.urls'))#富文本url
    path('user/', include('user.urls')),  # 用户url
    path('star/', include('star.urls')),  # 收藏url
    path('book/', include('book.urls')),  # 书籍url
    path('tinymce/', include('tinymce.urls')),  # 富文本url
    path('', include('FrontPage.urls')),  # TODO 待改book为主页 主页url，放最后降低搜索时间
]
