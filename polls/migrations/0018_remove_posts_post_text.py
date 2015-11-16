# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_remove_posts_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='post_text',
        ),
    ]
