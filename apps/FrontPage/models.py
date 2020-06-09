from django.db import models
# from django.contrib.auth.models import AbstractUserfrom
from tinymce.models import HTMLField
from db.base_model import BaseModel

# Create your models here.


# class user(AbstractUser, BaseModel):
# TODO 待改名为chapter的app

class chapter(BaseModel):
    chapter_id = models.IntegerField(
        verbose_name='章节编号', primary_key=True)
    text = HTMLField(verbose_name='章节正文')
    book_id = models.ForeignKey('book.Book', verbose_name='所属书籍',default='-1', on_delete=models.SET_DEFAULT)
    # TODO ondelete这块可以做文章
    chapter_img_url = models.CharField(
        verbose_name='章节图片', max_length=50, default='-1')
    chapter_introduction = models.CharField(
        verbose_name='章节介绍', max_length=500)
    chapter_hot_rate = models.IntegerField(verbose_name='章节热度')
    chapter_name = models.CharField(verbose_name='章节名称', max_length=50)
    user_id = models.ForeignKey('user.User',
                                verbose_name='作者姓名', default='-1', on_delete=models.SET_DEFAULT)
    chapter_word_count = models.IntegerField(
        verbose_name='字数统计')

    class Meta:
        db_table = 'chapter'
        verbose_name='章节库'
        verbose_name_plural=verbose_name

