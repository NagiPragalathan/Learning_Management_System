# Generated by Django 3.0.5 on 2023-03-02 17:06

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_auto_20230302_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoteCourse',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('course_id', models.CharField(max_length=50)),
                ('semester', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='category',
        ),
        migrations.RemoveField(
            model_name='course',
            name='description',
        ),
        migrations.RemoveField(
            model_name='course',
            name='semester',
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 2, 17, 6, 34, 843872, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='classrooms',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 2, 17, 6, 34, 843872, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ebook',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 3, 2, 17, 6, 34, 843872, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ebook',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.NoteCourse'),
        ),
    ]
