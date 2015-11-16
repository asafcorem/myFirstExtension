# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20151114_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='pub_date',
            field=models.IntegerField(default=datetime.datetime(2015, 11, 14, 19, 53, 17, 997000)),
        ),
    ]
