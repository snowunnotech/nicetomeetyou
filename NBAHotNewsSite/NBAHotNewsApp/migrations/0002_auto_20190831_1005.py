# Generated by Django 2.2.4 on 2019-08-31 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NBAHotNewsApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nbahotnews',
            name='id',
        ),
        migrations.AlterField(
            model_name='nbahotnews',
            name='NewsId',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
