# Generated by Django 3.0.3 on 2020-07-09 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_auto_20200709_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pothole',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
