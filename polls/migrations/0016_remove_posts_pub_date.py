# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_auto_20151114_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='pub_date',
        ),
    ]
