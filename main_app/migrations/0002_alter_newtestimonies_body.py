# Generated by Django 4.0.5 on 2023-03-29 19:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newtestimonies',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]