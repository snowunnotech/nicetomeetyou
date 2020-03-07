# Generated by Django 3.0.3 on 2020-03-03 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NBASpotNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(blank=True, default='', max_length=30)),
                ('report_time', models.DateTimeField()),
                ('report_source', models.CharField(blank=True, default='', max_length=30)),
                ('report_url', models.CharField(blank=True, default='', max_length=50)),
                ('photo_url', models.CharField(blank=True, default='', max_length=60)),
                ('content', models.TextField(default='')),
            ],
        ),
    ]
