# Generated by Django 2.1 on 2018-09-07 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myprofile', '0004_comments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='height_field',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='width_field',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
