# Generated by Django 3.1 on 2020-09-14 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitors', '0013_monitor_access_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='pm100_aqi',
        ),
    ]