# Generated by Django 4.2.1 on 2023-05-21 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='centersdb',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mobileno', models.CharField(max_length=10)),
                ('line1', models.CharField(max_length=50)),
                ('line2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6)),
                ('whfrom', models.CharField(max_length=8)),
                ('whto', models.CharField(max_length=8)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
