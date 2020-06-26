from django.urls import path, include,reverse
from django.conf.urls import url
from chapter.views import ChapterDetailView

urlpatterns = [
    path('Content/<str:chapter_id>/',
        ChapterDetailView.as_view(), name='ChapterContent')

]
