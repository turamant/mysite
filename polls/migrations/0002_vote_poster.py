# Generated by Django 4.0 on 2021-12-28 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='poster',
            field=models.ImageField(blank=True, upload_to='posters/'),
        ),
    ]