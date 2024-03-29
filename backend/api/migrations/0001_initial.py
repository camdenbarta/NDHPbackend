# Generated by Django 3.2.7 on 2021-11-14 22:44

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth'), ('Fifth', 'Fifth'), ('Sixth', 'Sixth')], default='First', max_length=20, verbose_name='Location on Page')),
                ('dateTimeCompleted', models.DateField(null=True, verbose_name='Date Completed/Updated')),
                ('title', models.CharField(max_length=50, null=True, verbose_name='Name Listed')),
                ('paragraph', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Paragraph/ Body')),
                ('bullet', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Bullet Point')),
            ],
            options={
                'verbose_name': 'About',
            },
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageName', models.CharField(max_length=50, null=True, verbose_name='Name of Image')),
                ('image', models.ImageField(blank=True, null=True, upload_to=api.models.nameFile)),
            ],
            options={
                'verbose_name': 'Carousel Image',
                'verbose_name_plural': 'Carousel Images',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('message', models.CharField(blank=True, max_length=350, null=True)),
            ],
            options={
                'verbose_name': 'Contact Form',
            },
        ),
        migrations.CreateModel(
            name='Image_Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True, verbose_name='Name Listed')),
                ('location', models.CharField(choices=[('About', 'About'), ('Archive', 'Archive'), ('Contact', 'Contact'), ('Home', 'Home'), ('Meet the Members', 'Meet the Members'), ('News Letter', 'News Letter'), ('Policy Positions', 'Policy Positions')], default='Home', max_length=20, verbose_name='Location in Website')),
                ('image', models.ImageField(blank=True, null=True, upload_to=api.models.nameFile)),
                ('video_URL', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Image or Video',
                'verbose_name_plural': 'Images or Videos',
            },
        ),
        migrations.CreateModel(
            name='Meet_Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth'), ('Fifth', 'Fifth'), ('Sixth', 'Sixth')], default='First', max_length=20, verbose_name='Location on Page')),
                ('dateTimeCompleted', models.DateField(null=True, verbose_name='Date Completed/Updated')),
                ('name', models.CharField(max_length=60, null=True, verbose_name="Member's Name")),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Position Title')),
                ('image', models.ImageField(blank=True, null=True, upload_to=api.models.nameFile)),
                ('about', models.TextField(blank=True, max_length=2000, null=True, verbose_name="Member's Bio")),
            ],
            options={
                'verbose_name': 'Meet the Member',
                'verbose_name_plural': 'Meet the Members',
            },
        ),
        migrations.CreateModel(
            name='News_Letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth'), ('Fifth', 'Fifth'), ('Sixth', 'Sixth')], default='First', max_length=20, verbose_name='Location on Page')),
                ('dateTimeCompleted', models.DateField(null=True, verbose_name='Date Completed/Updated')),
                ('title', models.CharField(max_length=30, null=True, verbose_name='Title of the Article')),
                ('author', models.CharField(blank=True, max_length=50, null=True, verbose_name='News Letter Author (Optional)')),
                ('body1', models.TextField(max_length=3000, null=True, verbose_name=' Body 1 --- Enter one paragraph at a time for page break')),
                ('body2', models.TextField(blank=True, max_length=3000, null=True, verbose_name=' Body 2 (Optional) --- Enter one paragraph at a time for page break')),
                ('body3', models.TextField(blank=True, max_length=3000, null=True, verbose_name=' Body 3 (Optional) --- Enter one paragraph at a time for page break')),
                ('body4', models.TextField(blank=True, max_length=3000, null=True, verbose_name=' Body 4 (Optional) --- Enter one paragraph at a time for page break')),
                ('body5', models.TextField(blank=True, max_length=3000, null=True, verbose_name=' Body 5 (Optional) --- Enter one paragraph at a time for page break')),
                ('bullet1', models.TextField(blank=True, max_length=260, null=True, verbose_name=' Bullet Points 1 (Optional) --- This will be after all of the paragraphs *Enter one at a time')),
                ('bullet2', models.TextField(blank=True, max_length=260, null=True, verbose_name=' Bullet Points 2 (Optional) --- This will be after all of the paragraphs *Enter one at a time')),
                ('bullet3', models.TextField(blank=True, max_length=260, null=True, verbose_name=' Bullet Points 3 (Optional) --- This will be after all of the paragraphs *Enter one at a time')),
                ('bullet4', models.TextField(blank=True, max_length=260, null=True, verbose_name=' Bullet Points 4 (Optional) --- This will be after all of the paragraphs *Enter one at a time')),
                ('bullet5', models.TextField(blank=True, max_length=260, null=True, verbose_name=' Bullet Points 5 (Optional) --- This will be after all of the paragraphs *Enter one at a time')),
            ],
            options={
                'verbose_name': 'News Letter',
                'verbose_name_plural': 'News Letters',
            },
        ),
        migrations.CreateModel(
            name='Party_Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth'), ('Fifth', 'Fifth'), ('Sixth', 'Sixth')], default='First', max_length=20, verbose_name='Location on Page')),
                ('dateTimeCompleted', models.DateField(null=True, verbose_name='Date Completed/Updated')),
                ('name', models.CharField(max_length=60, null=True, verbose_name='Name of Member')),
                ('email', models.CharField(max_length=100, null=True, verbose_name="Member's Email")),
                ('position', models.CharField(blank=True, max_length=60, null=True, verbose_name='Position Title (Optional)')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name="Member's Phone Number (Optional)")),
                ('city', models.CharField(blank=True, max_length=24, null=True, verbose_name="Member's Current City (Optional)")),
                ('state', models.CharField(blank=True, max_length=24, null=True, verbose_name="Member's Current State (Optional)")),
            ],
            options={
                'verbose_name': 'Party Contact',
                'verbose_name_plural': 'Party Contacts',
            },
        ),
        migrations.CreateModel(
            name='Policy_Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth'), ('Fifth', 'Fifth'), ('Sixth', 'Sixth')], default='First', max_length=20, verbose_name='Location on Page')),
                ('dateTimeCompleted', models.DateField(null=True, verbose_name='Date Completed/Updated')),
                ('position_name', models.CharField(max_length=60, null=True, verbose_name='Position Display Name')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Position Description (Optional)')),
                ('bullet1', models.TextField(blank=True, max_length=300, null=True, verbose_name='Position Bullet Points (Optional) --- This will be after the paragraph *Enter one at a time')),
                ('bullet2', models.TextField(blank=True, max_length=300, null=True, verbose_name='Position Bullet Points (Optional) --- This will be after the paragraph *Enter one at a time')),
                ('bullet3', models.TextField(blank=True, max_length=300, null=True, verbose_name='Position Bullet Points (Optional) --- This will be afterthe paragraph *Enter one at a time')),
                ('bullet4', models.TextField(blank=True, max_length=300, null=True, verbose_name='Position Bullet Points (Optional) --- This will be afterthe paragraph *Enter one at a time')),
            ],
            options={
                'verbose_name': 'Policy Position',
                'verbose_name_plural': 'Policy Positions',
            },
        ),
    ]
