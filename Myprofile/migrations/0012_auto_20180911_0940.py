# Generated by Django 2.1 on 2018-09-11 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myprofile', '0011_auto_20180910_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dislike',
            name='count_d',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='like',
            name='count_l',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
