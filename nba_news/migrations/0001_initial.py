# Generated by Django 2.2.2 on 2019-06-06 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
                ('img', models.CharField(max_length=200)),
                ('article', models.CharField(max_length=200)),
                ('video', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
