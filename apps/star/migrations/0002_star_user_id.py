# Generated by Django 3.0.7 on 2020-06-09 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('star', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='star',
            name='user_id',
            field=models.ForeignKey(default='-1', on_delete=django.db.models.deletion.SET_DEFAULT, to='user.User', verbose_name='??id'),
        ),
    ]
