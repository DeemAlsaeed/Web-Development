# Generated by Django 5.0.2 on 2024-04-30 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_profile_old_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='care',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]