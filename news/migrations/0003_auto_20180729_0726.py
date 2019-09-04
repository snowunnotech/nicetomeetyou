# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20180729_0037'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='newspost',
            table='newspost',
        ),
    ]
