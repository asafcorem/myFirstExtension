# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_groups_is_important'),
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(default=0)),
                ('group_id', models.IntegerField(default=0)),
                ('keyword', models.CharField(max_length=200)),
                ('post_text', models.TextField()),
                ('link', models.CharField(max_length=500)),
            ],
        ),
    ]
