# Generated by Django 3.2.7 on 2021-09-21 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='party_contact',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]