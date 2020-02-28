# Generated by Django 3.0.3 on 2020-02-27 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nba_news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nba_title', models.CharField(blank=True, default='', max_length=30)),
                ('nba_content', models.TextField(blank=True, default='')),
                ('nba_url', models.TextField(blank=True, default='')),
                ('nba_time', models.CharField(default='', max_length=50, null=True)),
            ],
        ),
    ]
