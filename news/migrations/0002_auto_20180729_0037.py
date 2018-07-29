# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newspost',
            old_name='content',
            new_name='para2',
        ),
        migrations.AddField(
            model_name='newspost',
            name='para1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='newspost',
            name='para3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='newspost',
            name='para4',
            field=models.TextField(blank=True),
        ),
    ]
