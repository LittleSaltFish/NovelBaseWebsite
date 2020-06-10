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
