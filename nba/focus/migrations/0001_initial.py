# Generated by Django 2.2.3 on 2019-07-28 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='文章標題')),
                ('author', models.CharField(max_length=128, verbose_name='文章作者')),
                ('body', models.TextField(verbose_name='內文')),
                ('abstract', models.TextField(blank=True, max_length=256, null=True, verbose_name='摘要')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='創建時間')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='創建時間')),
            ],
            options={
                'verbose_name': '焦點文章',
                'verbose_name_plural': '焦點文章',
                'ordering': ['-created_time'],
            },
        ),
    ]
