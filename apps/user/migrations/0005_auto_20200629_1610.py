# Generated by Django 3.0.7 on 2020-06-29 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200628_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star',
            name='star_statue',
            field=models.IntegerField(default=1, verbose_name='收藏状态'),
        ),
        migrations.CreateModel(
            name='Inform',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('inform_id', models.AutoField(primary_key=True, serialize=False, verbose_name='通知编号')),
                ('inform_flag', models.IntegerField(default=1, verbose_name='通知种类')),
                ('root_id', models.IntegerField(default=0, verbose_name='通知来源')),
                ('inform_statue', models.IntegerField(default=1, verbose_name='关系状态')),
                ('user_id', models.ForeignKey(default='-1', on_delete=django.db.models.deletion.SET_DEFAULT, to='user.User', verbose_name='用户')),
            ],
            options={
                'verbose_name': '通知库',
                'verbose_name_plural': '通知库',
                'db_table': 'inform',
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('fans_id', models.AutoField(primary_key=True, serialize=False, verbose_name='关系编号')),
                ('follow_statue', models.IntegerField(default=1, verbose_name='关系状态')),
                ('user_id1', models.ForeignKey(default='-1', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='用户主', to='user.User', verbose_name='用户主')),
                ('user_id2', models.ForeignKey(default='-1', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='用户从', to='user.User', verbose_name='用户从')),
            ],
            options={
                'verbose_name': '关系库',
                'verbose_name_plural': '关系库',
                'db_table': 'follow',
            },
        ),
    ]