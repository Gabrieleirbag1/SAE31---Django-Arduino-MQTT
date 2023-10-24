# Generated by Django 4.2.1 on 2023-10-13 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dubstep_app', '0007_pression_altitude'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plageshoraires',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_debut', models.DateTimeField()),
                ('datetime_fin', models.DateTimeField()),
                ('plages_on_off', models.BooleanField(null=True)),
                ('topicname', models.CharField(max_length=255)),
            ],
        ),
    ]