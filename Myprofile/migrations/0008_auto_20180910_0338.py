# Generated by Django 2.1 on 2018-09-09 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myprofile', '0007_auto_20180910_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='upload_location'),
        ),
    ]