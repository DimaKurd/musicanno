# Generated by Django 3.1.1 on 2020-11-17 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_song_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='requests',
            field=models.IntegerField(default=0),
        ),
    ]