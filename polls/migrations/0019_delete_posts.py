# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_remove_posts_post_text'),
    ]

    operations = [
        migrations.DeleteModel(
            name='posts',
        ),
    ]
