# Generated by Django 3.0.7 on 2020-06-09 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20200610_0145'),
        ('FrontPage', '0007_remove_chapter_book_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='book_id',
            field=models.ForeignKey(default='-1', on_delete=django.db.models.deletion.SET_DEFAULT, to='book.Book', verbose_name='所属书籍'),
        ),
    ]
