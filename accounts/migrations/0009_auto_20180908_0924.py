# Generated by Django 2.1 on 2018-09-08 03:54

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20180908_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='/media/profile.png', upload_to=accounts.models.upload_location),
        ),
    ]