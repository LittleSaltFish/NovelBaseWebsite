from django.urls import path, include,reverse
from django.conf.urls import url
from chapter.views import ChapterDetailView

urlpatterns = [
    url(r'^Content/(?P<chapter_id>\d+)',
        ChapterDetailView.as_view(), name='BookDetail')

]
