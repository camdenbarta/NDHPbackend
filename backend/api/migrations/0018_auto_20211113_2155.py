# Generated by Django 3.2.7 on 2021-11-13 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20211113_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carousel',
            name='dateTimeCompleted',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='order_no',
        ),
    ]
