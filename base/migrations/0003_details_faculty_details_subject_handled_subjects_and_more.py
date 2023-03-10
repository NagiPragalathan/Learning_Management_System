# Generated by Django 4.0.1 on 2023-01-21 11:47

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_member_id_roommember_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_id', models.IntegerField()),
                ('image', models.ImageField(default='images/user_image.png', upload_to='photo/%Y/%m/%d')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField(default=datetime.datetime(2023, 1, 21, 11, 47, 5, 1606, tzinfo=utc))),
                ('designation', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=200)),
                ('coming_from', models.CharField(max_length=200)),
                ('mail_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty_details',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=200, unique=True)),
                ('image', models.ImageField(default='images/Screenshot_3.png', upload_to='photo/%Y/%m/%d')),
                ('id_number', models.IntegerField()),
                ('name', models.CharField(max_length=200, unique=True)),
                ('designation', models.CharField(default='designation', max_length=200)),
                ('date_of_join', models.DateField(default=datetime.datetime(2023, 1, 21, 11, 47, 5, 607, tzinfo=utc))),
                ('department', models.CharField(default='department', max_length=200)),
                ('qualififcation', models.CharField(default='qualififcation', max_length=200)),
                ('assessment_period', models.IntegerField(default=0)),
                ('experience', models.IntegerField(default=0)),
                ('bio', models.CharField(default='No Bio yet.', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subject_handled',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_id', models.IntegerField()),
                ('subject_name', models.CharField(max_length=200)),
                ('subject_code', models.CharField(max_length=200)),
                ('target_pass', models.CharField(default='10', max_length=200)),
                ('actual_pass', models.CharField(default='10', max_length=200)),
                ('subject_staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.faculty_details')),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_image', models.CharField(max_length=200)),
                ('subject_name', models.CharField(max_length=200, unique=True)),
                ('subject_code', models.CharField(max_length=200, unique=True)),
                ('semester', models.IntegerField()),
                ('department', models.CharField(max_length=200)),
                ('discription', models.CharField(default='No Discription yet.', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=200, unique=True)),
                ('mail_id', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200, unique=True)),
                ('role', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Test_evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=200)),
                ('target_pass', models.CharField(max_length=200)),
                ('actual_pass', models.CharField(max_length=200)),
                ('subject_detials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.subject_handled')),
            ],
        ),
        migrations.AddField(
            model_name='faculty_details',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.users'),
        ),
    ]
