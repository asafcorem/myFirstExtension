# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0026_auto_20151119_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scans',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_of_the_scan', models.IntegerField()),
            ],
        ),
    ]
