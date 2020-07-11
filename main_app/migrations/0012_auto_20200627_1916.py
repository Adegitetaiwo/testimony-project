# Generated by Django 3.0.6 on 2020-06-27 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200626_1338'),
        ('main_app', '0011_auto_20200627_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='newtestimonies',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='account.publicUser', verbose_name=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newtestimonies',
            name='author',
            field=models.CharField(max_length=50),
        ),
    ]
