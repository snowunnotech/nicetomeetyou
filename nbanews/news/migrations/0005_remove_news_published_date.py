# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_published_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='published_date',
        ),
    ]
