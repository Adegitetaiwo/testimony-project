# Generated by Django 3.0.8 on 2020-07-15 00:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0033_auto_20200710_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newtestimonies',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
