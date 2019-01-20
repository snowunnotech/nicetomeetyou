# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_auto_20180831_2356'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-post_date',)},
        ),
    ]
