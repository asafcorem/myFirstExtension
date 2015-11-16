# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20151106_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='is_important',
            field=models.IntegerField(default=0),
        ),
    ]
