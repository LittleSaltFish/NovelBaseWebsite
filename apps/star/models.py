from django.db import models
from db.base_model import BaseModel

# Create your models here.


class Star(BaseModel):
    '''收藏类'''
    # NOTE 可能会整合到user里
    star_id = models.IntegerField(
        verbose_name='收藏编号', primary_key=True)
    user_id = models.ForeignKey('user.User',
                                verbose_name='用户', default='-1', on_delete=models.SET_DEFAULT)
    book_id = models.ForeignKey('book.Book',
                                verbose_name='书籍编号', default='-1', on_delete=models.SET_DEFAULT)
    book_mark = models.IntegerField(
        verbose_name='书签位置')

    class Meta:
        db_table = 'df_star'
        verbose_name = '收藏库'
        verbose_name_plural = verbose_name
