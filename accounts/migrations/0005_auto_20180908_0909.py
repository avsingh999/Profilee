# Generated by Django 2.1 on 2018-09-08 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180908_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile.png', height_field='height_field', upload_to='dp', width_field='width_field'),
        ),
    ]