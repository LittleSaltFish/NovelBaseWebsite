from django.db import models
from db.base_model import BaseModel

# Create your models here.


class Book(BaseModel):
    '''书籍类'''
    book_id = models.IntegerField(
        verbose_name='书籍编号', primary_key=True)
    book_img_url = models.CharField(
        verbose_name='书籍图片', max_length=50, default='-1')
    book_introduction = models.CharField(
        verbose_name='书籍介绍', max_length=500)
    book_hot_rate = models.IntegerField(verbose_name='书籍热度')
    book_name = models.CharField(verbose_name='书籍名称', max_length=50)
    user_id = models.ForeignKey('user.User',
                                verbose_name='作者姓名',default='-1', on_delete=models.SET_DEFAULT)
    book_word_count = models.IntegerField(
        verbose_name='字数统计')

    class Meta:
        db_table = 'book'
        verbose_name = '书籍信息库'
        verbose_name_plural = verbose_name
