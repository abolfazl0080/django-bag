# Generated by Django 5.0.6 on 2024-05-20 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'کاربر', 'verbose_name_plural': 'کاربران'},
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='', max_length=11, verbose_name='شماره تلفن'),
        ),
    ]
