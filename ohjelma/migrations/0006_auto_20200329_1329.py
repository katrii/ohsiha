# Generated by Django 3.0.2 on 2020-03-29 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ohjelma', '0005_auto_20200329_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='track_duration',
            field=models.CharField(max_length=10),
        ),
    ]
