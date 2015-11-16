# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_all_groups_user_belong'),
    ]

    operations = [
        migrations.CreateModel(
            name='groups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(max_length=200)),
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
        migrations.RemoveField(
            model_name='all_groups_user_belong',
            name='question',
        ),
        migrations.DeleteModel(
            name='All_groups_user_belong',
        ),
        migrations.AddField(
            model_name='groups',
            name='user_own',
            field=models.ForeignKey(to='polls.Users'),
        ),
    ]
