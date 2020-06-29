from django.contrib import admin
from chapter.models import Chapter, TagMassage, Tag,ChapterComment
# Register your models here.

admin.site.register(Chapter)
admin.site.register(Tag)
admin.site.register(ChapterComment)
admin.site.register(TagMassage)
