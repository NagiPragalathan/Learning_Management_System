# Generated by Django 3.2.4 on 2023-01-23 19:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_auto_20230124_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 23, 19, 10, 31, 936947, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='faculty_details',
            name='date_of_join',
            field=models.DateField(default=datetime.datetime(2023, 1, 23, 19, 10, 31, 936947, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 23, 19, 10, 31, 936947, tzinfo=utc)),
        ),
    ]
