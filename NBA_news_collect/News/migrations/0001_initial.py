# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=250)),
                ('image_url', models.CharField(max_length=250)),
                ('detail_url', models.CharField(max_length=250)),
                ('post_date', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('detail', models.CharField(max_length=600)),
                ('video_url', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
