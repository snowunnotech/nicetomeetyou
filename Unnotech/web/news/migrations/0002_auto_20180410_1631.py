# Generated by Django 2.0.4 on 2018-04-10 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image_url',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='news',
            name='url',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
