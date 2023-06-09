# Generated by Django 4.2.2 on 2023-06-10 20:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centers', '0006_alter_centersdb_created_alter_entries_entrydatetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='centersdb',
            name='slot1',
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='centersdb',
            name='slot2',
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='centersdb',
            name='whfrom',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='centersdb',
            name='whto',
            field=models.TimeField(),
        ),
    ]
