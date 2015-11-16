# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_auto_20151115_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 15, 16, 59, 30, 660000)),
        ),
    ]
