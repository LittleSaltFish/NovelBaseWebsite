from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    '''模型抽象基类'''
    create_time=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    #NOTE 生成时要加默认时间，timezone.now()
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')

    class Meta:
        '''抽象模型类'''
        abstract=True
