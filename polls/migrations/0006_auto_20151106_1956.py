# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20151104_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groups',
            name='user_own',
        ),
        migrations.DeleteModel(
            name='groups',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
