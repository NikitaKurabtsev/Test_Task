# Generated by Django 3.2.7 on 2021-10-26 17:18

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20211026_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='update',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 20, 18, 20, 322233)),
        ),
    ]
