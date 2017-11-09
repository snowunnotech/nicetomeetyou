# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_remove_news_published_date'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='news',
            table='news',
        ),
    ]
