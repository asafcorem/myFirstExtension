# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(max_length=200)),
                ('group_link', models.CharField(default=b'default', max_length=200)),
                ('is_important', models.IntegerField(default=0)),
                ('keyword', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(default=0)),
                ('group_id', models.IntegerField(default=0)),
                ('keyword', models.CharField(max_length=200)),
                ('post_text', models.TextField()),
                ('link', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2015, 11, 15, 16, 58, 32, 491000))),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_mail', models.CharField(max_length=200)),
                ('user_password', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='groups',
            name='user_own',
            field=models.ForeignKey(to='polls.Users'),
        ),
    ]
