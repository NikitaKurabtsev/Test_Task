# Generated by Django 3.2.7 on 2021-10-26 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_alter_record_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='update',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]