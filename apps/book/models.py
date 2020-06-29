from django.db import models
from db.base_model import BaseModel
from tinymce.models import HTMLField

# Create your models here.


class Book(BaseModel):
    '''书籍类'''
    book_id = models.AutoField(
        verbose_name='书籍编号', primary_key=True)
    book_img_url = models.URLField(
        verbose_name='书籍图片', default='-1')
    book_introduction = models.CharField(
        verbose_name='书籍介绍', max_length=500)
    book_hot_rate = models.IntegerField(verbose_name='书籍热度')
    book_name = models.CharField(verbose_name='书籍名称', max_length=50)
    user_id = models.ForeignKey('user.User',
                                verbose_name='作者',default='-1', on_delete=models.SET_DEFAULT)
    book_word_count = models.IntegerField(
        verbose_name='字数统计')
    book_statue = models.IntegerField(verbose_name='书籍状态', default=-1)
    # NOTE -2 已删除 -1 非公开 0 正在审核 1 公开未完结 2公开已完结

    class Meta:
        db_table = 'book'
        verbose_name = '书籍信息库'
        verbose_name_plural = verbose_name

class BookComment(BaseModel):
    comment_id: models.AutoField(
        verbose_name='评论编号', primary_key=True)
    book_id: models.ForeignKey(
        'book.Book', verbose_name='所属书籍', default='-1', on_delete=models.SET_DEFAULT)
    comment_content: HTMLField(verbose_name='评论正文')
    user_id: models.ForeignKey(
        'user.User', verbose_name='用户id', default='-1', on_delete=models.SET_DEFAULT)
    comment_statue = models.IntegerField(verbose_name='评论状态', default=-1)
    # NOTE -2 已删除 -1 有不良内容 1 公开 2置顶

    class Meta:
        db_table = 'book_comment'
        verbose_name = '书籍评论库'
        verbose_name_plural = verbose_name
