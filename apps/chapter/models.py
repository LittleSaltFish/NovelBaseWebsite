from django.db import models
# from django.contrib.auth.models import AbstractUserfrom
from tinymce.models import HTMLField
from db.base_model import BaseModel

# Create your models here.


class Chapter(BaseModel):
    chapter_id = models.AutoField(
        verbose_name='章节编号', primary_key=True)
    chapter_content = HTMLField(verbose_name='章节正文')
    book_id = models.ForeignKey(
        'book.Book', verbose_name='所属书籍', default='-1', on_delete=models.SET_DEFAULT)
    # TODO ondelete这块可以做文章
    chapter_img_url = models.URLField(
        verbose_name='章节图片', default='-1')
    chapter_introduction = models.CharField(
        verbose_name='章节介绍', max_length=500)
    chapter_hot_rate = models.IntegerField(verbose_name='章节热度')
    chapter_name = models.CharField(verbose_name='章节名称', max_length=50)
    user_id = models.ForeignKey('user.User',
                                verbose_name='作者', default='-1', on_delete=models.SET_DEFAULT)
    chapter_word_count = models.IntegerField(
        verbose_name='字数统计')
    chapter_position = models.IntegerField(verbose_name='章节位置')
    chapter_statue = models.IntegerField(verbose_name='章节状态', default=-1)
    # NOTE -2 已删除 -1 非公开 0 正在审核 1 公开

    class Meta:
        db_table = 'chapter'
        verbose_name = '章节库'
        verbose_name_plural = verbose_name

# TODO 推荐表

class ChapterComment(BaseModel):
    comment_id: models.AutoField(
        verbose_name='评论编号', primary_key=True)
    chapter_id: models.ForeignKey(
        'chapter.Chapter', verbose_name='所属章节', default='-1', on_delete=models.SET_DEFAULT)
    book_id: models.ForeignKey(
        'book.Book', verbose_name='所属书籍', default='-1', on_delete=models.SET_DEFAULT)
    comment_content: HTMLField(verbose_name='评论正文')
    user_id: models.ForeignKey(
        'user.User', verbose_name='用户id', default='-1', on_delete=models.SET_DEFAULT)
    comment_statue = models.IntegerField(verbose_name='评论状态', default=-1)
    # NOTE -2 已删除 -1 有不良内容 1 公开 2置顶

    class Meta:
        db_table = 'chapter_comment'
        verbose_name = '章节评论库'
        verbose_name_plural = verbose_name


class Tag(BaseModel):
    tag_id: models.AutoField(
        verbose_name='标签编号', primary_key=True)
    chapter_id: models.ForeignKey(
        'chapter.Chapter', verbose_name='所属章节', default='-1', on_delete=models.SET_DEFAULT)
    book_id: models.ForeignKey(
        'book.Book', verbose_name='所属书籍', default='-1', on_delete=models.SET_DEFAULT)
    tag_statue = models.IntegerField(verbose_name='标签状态', default=-1)
    # NOTE -1 已删除 1 公开

    class Meta:
        db_table = 'tag'
        verbose_name = '标签库'
        verbose_name_plural = verbose_name

class TagMassage(BaseModel):
    tag_id: models.AutoField(
        verbose_name='标签详情编号', primary_key=True)
    tag_hot_rate = models.IntegerField(verbose_name='标签热度', default=-1)
    tag_name = models.CharField(verbose_name='标签名称',max_length=50, default=-1)
    tag_statue = models.IntegerField(verbose_name='标签状态', default=-1)
    # NOTE -1 已删除 1 公开

    class Meta:
        db_table = 'tag_massage'
        verbose_name = '标签详情库'
        verbose_name_plural = verbose_name
