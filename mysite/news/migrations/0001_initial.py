# Generated by Django 2.2.4 on 2019-08-05 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HotNews',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=100)),
                ('published_datetime', models.CharField(max_length=100)),
                ('contents', models.TextField()),
            ],
        ),
    ]
