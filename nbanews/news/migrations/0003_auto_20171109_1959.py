# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20171109_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pic_url',
            field=models.URLField(),
        ),
    ]
