# Generated by Django 3.0.6 on 2020-07-10 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0032_auto_20200706_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='biblequote',
            name='verse',
            field=models.CharField(default=None, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newtestimonies',
            name='category',
            field=models.CharField(choices=[('choose', 'Choose'), ('salvation', 'Salvation'), ('health', 'Health'), ('addiction', 'Addiction'), ('finance', 'Finance'), ('protection', 'Protection'), ('others', 'Others')], max_length=150),
        ),
    ]
