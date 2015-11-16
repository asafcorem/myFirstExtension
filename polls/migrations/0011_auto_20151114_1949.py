# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_posts_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2015, 11, 14, 19, 49, 13, 427000)),
        ),
    ]
