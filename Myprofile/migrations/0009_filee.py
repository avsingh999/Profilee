# Generated by Django 2.1 on 2018-09-10 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myprofile', '0008_auto_20180910_0338'),
    ]

    operations = [
        migrations.CreateModel(
            name='FILEE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(upload_to='testfile')),
            ],
        ),
    ]