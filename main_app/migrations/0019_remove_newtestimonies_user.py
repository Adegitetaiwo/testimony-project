# Generated by Django 3.0.6 on 2020-06-28 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_newtestimonies_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newtestimonies',
            name='user',
        ),
    ]
