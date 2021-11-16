# Generated by Django 3.2.7 on 2021-10-26 15:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20211025_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update', models.DateTimeField(auto_now_add=True)),
                ('record_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='record_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Table',
        ),
    ]