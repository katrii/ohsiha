# Generated by Django 3.0.2 on 2020-03-13 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ohjelma', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=200)),
                ('song_artist', models.CharField(max_length=200)),
            ],
        ),
    ]
