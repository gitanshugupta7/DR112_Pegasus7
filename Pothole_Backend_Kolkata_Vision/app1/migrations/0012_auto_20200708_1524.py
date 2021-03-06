# Generated by Django 3.0.3 on 2020-07-08 09:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_auto_20200708_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='uploaded_timestamp',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='pothole',
            name='completed_timestamp',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='pothole',
            name='ongoin_timestamp',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='pothole',
            name='uploaded_timestamp',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
