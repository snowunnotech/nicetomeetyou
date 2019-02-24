# Generated by Django 2.1.7 on 2019-02-23 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('uuid', models.CharField(blank=True, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=20)),
                ('published_date', models.TextField()),
                ('text', models.TextField()),
            ],
        ),
    ]
