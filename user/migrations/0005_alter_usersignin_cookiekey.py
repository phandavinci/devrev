# Generated by Django 4.2.1 on 2023-05-21 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_usersignin_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersignin',
            name='cookiekey',
            field=models.CharField(default='0', max_length=45),
        ),
    ]
