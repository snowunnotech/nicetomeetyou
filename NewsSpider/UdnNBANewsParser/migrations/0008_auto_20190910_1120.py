# Generated by Django 2.2.5 on 2019-09-10 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UdnNBANewsParser', '0007_nbanews_is_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nbanews',
            name='content',
            field=models.TextField(max_length=10000, verbose_name='content'),
        ),
    ]
