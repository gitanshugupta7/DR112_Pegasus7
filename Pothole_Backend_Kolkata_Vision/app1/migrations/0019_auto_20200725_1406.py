# Generated by Django 3.0.3 on 2020-07-25 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_auto_20200710_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pothole',
            name='no_of_reporters',
            field=models.IntegerField(default=1),
        ),
    ]
