# Generated by Django 4.2.1 on 2023-05-22 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_usersignin_mobileno_alter_usersignin_name'),
        ('centers', '0004_remove_entries_userno'),
    ]

    operations = [
        migrations.AddField(
            model_name='entries',
            name='userno',
            field=models.ForeignKey(default='Abishek', on_delete=django.db.models.deletion.CASCADE, to='user.usersignin'),
            preserve_default=False,
        ),
    ]
