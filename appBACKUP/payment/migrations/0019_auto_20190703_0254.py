# Generated by Django 2.2 on 2019-07-03 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0018_auto_20190627_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guesttemporaryinfo',
            name='id',
            field=models.CharField(default='ae719d1f', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
