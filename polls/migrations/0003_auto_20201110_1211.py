# Generated by Django 3.1.1 on 2020-11-10 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20201110_0942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mark',
            old_name='song_id',
            new_name='song',
        ),
        migrations.AddField(
            model_name='song',
            name='album_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(default='', max_length=10),
        ),
    ]
