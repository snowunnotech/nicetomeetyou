# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20180729_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
