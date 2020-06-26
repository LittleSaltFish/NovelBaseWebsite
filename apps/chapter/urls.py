from django.urls import path, include,reverse
from django.conf.urls import url
from chapter.views import ChapterDetailView

urlpatterns = [
    path('book/<str:book_id_id>/chapter/<str:chapter_id>/',
        ChapterDetailView.as_view(), name='ChapterContent')

]
