# Generated by Django 3.1.1 on 2020-11-10 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20201110_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='link',
        ),
    ]
