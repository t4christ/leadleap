# Generated by Django 2.0 on 2019-06-22 11:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ldtkc', '0018_auto_20190622_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='mobile',
            field=models.CharField(blank=True, max_length=13, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='start_course',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 17, 11, 20, 52, 287607)),
        ),
    ]
