# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0025_auto_20151115_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='pub_date',
            field=models.IntegerField(),
        ),
    ]
