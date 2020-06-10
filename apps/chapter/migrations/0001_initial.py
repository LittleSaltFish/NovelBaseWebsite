# Generated by Django 3.0.7 on 2020-06-10 07:26

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0004_auto_20200610_1426'),
        ('user', '0002_auto_20200610_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('chapter_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='章节编号')),
                ('text', tinymce.models.HTMLField(verbose_name='章节正文')),
                ('chapter_img_url', models.CharField(default='-1', max_length=50, verbose_name='章节图片')),
                ('chapter_introduction', models.CharField(max_length=500, verbose_name='章节介绍')),
                ('chapter_hot_rate', models.IntegerField(verbose_name='章节热度')),
                ('chapter_name', models.CharField(max_length=50, verbose_name='章节名称')),
                ('chapter_word_count', models.IntegerField(verbose_name='字数统计')),
                ('book_id', models.ForeignKey(default='-1', on_delete=django.db.models.deletion.SET_DEFAULT, to='book.Book', verbose_name='所属书籍')),
                ('user_id', models.ForeignKey(default='-1', on_delete=django.db.models.deletion.SET_DEFAULT, to='user.User', verbose_name='作者姓名')),
            ],
            options={
                'verbose_name': '章节库',
                'verbose_name_plural': '章节库',
                'db_table': 'chapter',
            },
        ),
    ]
