# Generated by Django 4.2.1 on 2023-10-12 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dubstep_app', '0005_temp_topicname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Humitide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humidite', models.FloatField(null=True)),
                ('date', models.CharField(max_length=255)),
                ('topicname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pression',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pression', models.FloatField(null=True)),
                ('date', models.CharField(max_length=255)),
                ('topicname', models.CharField(max_length=255)),
            ],
        ),
    ]
