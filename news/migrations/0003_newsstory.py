# Generated by Django 2.2.4 on 2019-08-08 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190806_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb_like', models.IntegerField()),
                ('author', models.CharField(default='', max_length=50)),
                ('payload', models.TextField(default='')),
                ('vedioUrl', models.URLField(default='')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News')),
            ],
        ),
    ]
