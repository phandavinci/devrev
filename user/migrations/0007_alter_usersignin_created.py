# Generated by Django 4.2.1 on 2023-05-23 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_usersignin_mobileno_alter_usersignin_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersignin',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='EntryDateTime'),
        ),
    ]
