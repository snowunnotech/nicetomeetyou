# Generated by Django 3.0.3 on 2020-03-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20200303_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='nbaspotnews',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]
