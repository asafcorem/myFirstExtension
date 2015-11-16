# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_auto_20151115_1304'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
