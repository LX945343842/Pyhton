# Generated by Django 2.1.7 on 2019-04-24 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_info', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movieinfo',
            old_name='mActors',
            new_name='mQuote',
        ),
        migrations.RenameField(
            model_name='movieinfo',
            old_name='mType',
            new_name='mScore',
        ),
    ]