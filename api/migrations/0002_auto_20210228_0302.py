# Generated by Django 3.1.7 on 2021-02-28 03:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='available_date',
            field=models.DateField(default=datetime.datetime(2021, 2, 28, 3, 2, 50, 203474, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='start_time',
            field=models.TimeField(),
        ),
    ]