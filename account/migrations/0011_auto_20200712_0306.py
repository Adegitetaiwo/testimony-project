# Generated by Django 3.0.8 on 2020-07-12 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20200702_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicuser',
            name='city',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='publicuser',
            name='country',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='publicuser',
            name='gender',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='publicuser',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='publicuser',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]