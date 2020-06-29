from django.db import models
from db.base_model import BaseModel
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser,BaseModel):
    # TODO此处用的现成的模型，用户名不能重复，考虑自建模型
    
    
    class Meta:
        db_table='user'
        verbose_name='用户库'
        verbose_name_plural=verbose_name

class Star(BaseModel):
    '''收藏类'''
    # NOTE 可能会整合到user里
    star_id = models.AutoField(
        verbose_name='收藏编号', primary_key=True)
    user_id = models.ForeignKey('user.User',
                                verbose_name='用户', default='-1', on_delete=models.SET_DEFAULT)
    book_id = models.ForeignKey('book.Book',
                                verbose_name='书籍编号', default='-1', on_delete=models.SET_DEFAULT)
    book_mark = models.IntegerField(
        verbose_name='书签位置', default=0)
    star_statue = models.IntegerField(verbose_name='收藏状态', default=1)
    # NOTE -2 已删除 -1 非公开 1 公开

    class Meta:
        db_table = 'star'
        verbose_name = '收藏库'
        verbose_name_plural = verbose_name

class Follow(BaseModel):
    '''粉丝类'''
    fans_id=models.AutoField(
        verbose_name='关系编号', primary_key=True)
    user_id1 = models.ForeignKey('user.User',
                                 verbose_name='用户主', default='-1', on_delete=models.SET_DEFAULT, related_name='用户主')
    user_id2 = models.ForeignKey('user.User',
                                 verbose_name='用户从', default='-1', on_delete=models.SET_DEFAULT, related_name='用户从')
    follow_statue = models.IntegerField(verbose_name='关系状态', default=1)
    # NOTE -2 已删除 -1 非公开 1 公开
    class Meta:
        db_table = 'follow'
        verbose_name = '关系库'
        verbose_name_plural = verbose_name


class Inform(BaseModel):
    '''通知类'''
    inform_id=models.AutoField(
        verbose_name='通知编号', primary_key=True)
    inform_flag = models.IntegerField(verbose_name='通知种类', default=1)
    root_id = models.IntegerField(verbose_name='通知来源', default=0)
    # NOTE 为0时不显示，为未知通知
    user_id = models.ForeignKey('user.User',
                                 verbose_name='用户', default='-1', on_delete=models.SET_DEFAULT)
    inform_statue = models.IntegerField(verbose_name='关系状态', default=1)
    # NOTE -2 已删除 -1 非公开 1 公开
    class Meta:
        db_table = 'inform'
        verbose_name = '通知库'
        verbose_name_plural = verbose_name


