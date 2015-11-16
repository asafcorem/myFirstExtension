# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20151106_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(max_length=200)),
                ('group_link', models.CharField(default=b'default', max_length=200)),
                ('keyword', models.CharField(max_length=200)),
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
