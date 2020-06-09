from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

urlpatterns = [
    path('', include('FrontPage.urls')),#主页url
    path('admin/', admin.site.urls),#管理url
    # url(r'^tinymce/',include('tinymce.urls'))#富文本url
    path('tinymce/', include('tinymce.urls'))#富文本url
]
