# Generated by Django 2.2.4 on 2019-08-26 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0002_news_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
