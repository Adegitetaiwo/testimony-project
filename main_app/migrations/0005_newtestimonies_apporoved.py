# Generated by Django 3.0.6 on 2020-06-26 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200626_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='newtestimonies',
            name='Apporoved',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
