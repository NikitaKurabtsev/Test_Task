# Generated by Django 3.2.7 on 2021-10-27 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_alter_contact_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
