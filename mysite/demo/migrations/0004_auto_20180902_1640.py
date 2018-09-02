# Generated by Django 2.1.1 on 2018-09-02 08:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ul',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
