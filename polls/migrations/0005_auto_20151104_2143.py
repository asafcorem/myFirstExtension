# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20151104_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groups',
            name='id',
        ),
        migrations.AddField(
            model_name='groups',
            name='group_link',
            field=models.CharField(default=b'default', max_length=200, serialize=False, primary_key=True),
        ),
    ]
