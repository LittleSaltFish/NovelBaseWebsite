# Generated by Django 3.0.7 on 2020-06-28 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20200610_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_statue',
            field=models.IntegerField(default=-1, verbose_name='书籍状态'),
        ),
    ]
