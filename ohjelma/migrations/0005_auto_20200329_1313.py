# Generated by Django 3.0.2 on 2020-03-29 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ohjelma', '0004_track'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='track_duration',
            field=models.CharField(max_length=5),
        ),
    ]
