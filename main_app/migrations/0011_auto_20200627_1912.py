# Generated by Django 3.0.6 on 2020-06-27 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200626_1338'),
        ('main_app', '0010_newtestimonies_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newtestimonies',
            name='user',
        ),
        migrations.AlterField(
            model_name='newtestimonies',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.publicUser', verbose_name=''),
        ),
    ]
