# Generated by Django 5.1.4 on 2025-01-10 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='payment_time',
        ),
    ]
