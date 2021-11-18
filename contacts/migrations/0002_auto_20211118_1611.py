# Generated by Django 3.2.7 on 2021-11-18 14:11

import contacts.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='comment',
            field=models.TextField(blank=True, default='', max_length=150, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create date'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='file',
            field=models.FileField(help_text='load pdf or doc document', upload_to=contacts.models._upload_file_cv, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc'])], verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='is_sent',
            field=models.BooleanField(default=False, verbose_name='feedback is sent'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='record',
            name='update',
            field=models.DateTimeField(auto_now=True, verbose_name='last query date'),
        ),
    ]