# Generated by Django 3.0.3 on 2020-07-08 08:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20200705_1115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='complaint',
            options={},
        ),
        migrations.AlterModelOptions(
            name='twitter_data',
            options={},
        ),
        migrations.RenameField(
            model_name='complaint',
            old_name='uploaded_time',
            new_name='uploaded_timestamp',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='uploaded_from',
        ),
        migrations.RemoveField(
            model_name='pothole',
            name='image',
        ),
        migrations.RemoveField(
            model_name='twitter_data',
            name='address',
        ),
        migrations.RemoveField(
            model_name='twitter_data',
            name='coordinates',
        ),
        migrations.RemoveField(
            model_name='twitter_data',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='twitter_data',
            name='pothole_image',
        ),
        migrations.AddField(
            model_name='complaint',
            name='origin',
            field=models.CharField(blank='True', default='', max_length=32),
        ),
        migrations.AddField(
            model_name='pothole',
            name='address',
            field=models.CharField(blank='True', default='', max_length=512),
        ),
        migrations.AddField(
            model_name='pothole',
            name='completed_timestamp',
            field=models.DateTimeField(blank='True', default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pothole',
            name='coordinates',
            field=models.CharField(blank='True', default='', max_length=64),
        ),
        migrations.AddField(
            model_name='pothole',
            name='ongoin_timestamp',
            field=models.DateTimeField(blank='True', default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pothole',
            name='uploaded_timestamp',
            field=models.DateTimeField(blank='True', default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twitter_data',
            name='complaint_id',
            field=models.CharField(blank='True', default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='address',
            field=models.CharField(blank='True', default='', max_length=1024),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='complaint_id',
            field=models.CharField(blank='True', default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='coordinates',
            field=models.CharField(blank='True', default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='pothole_image',
            field=models.URLField(blank='True', default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='pothole',
            name='complaint_id',
            field=models.CharField(blank='True', default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='pothole',
            name='status',
            field=models.CharField(default='Recent', max_length=20),
        ),
        migrations.AlterField(
            model_name='twitter_data',
            name='name',
            field=models.CharField(blank='True', default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='twitter_data',
            name='tweet_id',
            field=models.CharField(blank='True', default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='twitter_data',
            name='username',
            field=models.CharField(blank='True', default='', max_length=128),
        ),
    ]
