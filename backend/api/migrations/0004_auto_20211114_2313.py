# Generated by Django 3.2.7 on 2021-11-14 23:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211114_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 11, 14, 23, 13, 15, 649263, tzinfo=utc), verbose_name='Created on'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 11, 14, 23, 13, 21, 362636, tzinfo=utc), verbose_name='Submitted on'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image_video',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 11, 14, 23, 13, 27, 978694, tzinfo=utc), verbose_name='Created on'),
            preserve_default=False,
        ),
    ]
