# Generated by Django 5.0.2 on 2024-04-14 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_date2_imgaes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date',
            name='customer',
        ),
    ]
