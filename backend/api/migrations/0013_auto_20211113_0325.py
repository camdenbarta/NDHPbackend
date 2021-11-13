# Generated by Django 3.2.7 on 2021-11-13 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_rename_bullet_policy_position_bullet_point'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'About NDHP'},
        ),
        migrations.AlterModelOptions(
            name='archive',
            options={'verbose_name': 'Archive', 'verbose_name_plural': 'Archives'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact Form'},
        ),
        migrations.AlterModelOptions(
            name='meet_member',
            options={'verbose_name': 'Meet the Member', 'verbose_name_plural': 'Meet the Members'},
        ),
        migrations.AlterModelOptions(
            name='news_letter',
            options={'verbose_name': 'News Letter', 'verbose_name_plural': 'News Letters'},
        ),
        migrations.AlterModelOptions(
            name='party_contact',
            options={'verbose_name': 'Party Contact', 'verbose_name_plural': 'Party Contacts'},
        ),
        migrations.AlterModelOptions(
            name='policy_position',
            options={'verbose_name': 'Policy Position', 'verbose_name_plural': 'Policy Positions'},
        ),
    ]
