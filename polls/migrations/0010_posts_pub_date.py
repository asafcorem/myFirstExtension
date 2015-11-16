# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='pub_date',
            field=models.DateField(default = datetime.datetime.now()),
        ),
    ]
