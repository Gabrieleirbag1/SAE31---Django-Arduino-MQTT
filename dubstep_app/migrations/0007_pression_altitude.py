# Generated by Django 4.2.1 on 2023-10-13 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dubstep_app', '0006_humitide_pression'),
    ]

    operations = [
        migrations.AddField(
            model_name='pression',
            name='altitude',
            field=models.FloatField(null=True),
        ),
    ]
