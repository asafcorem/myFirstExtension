# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_remove_posts_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='link',
        ),
    ]