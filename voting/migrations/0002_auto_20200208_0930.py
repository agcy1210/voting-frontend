# Generated by Django 3.0.3 on 2020-02-08 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voter',
            old_name='vote_publickey',
            new_name='voter_publickey',
        ),
        migrations.AddField(
            model_name='voter',
            name='is_varified',
            field=models.BooleanField(default=False),
        ),
    ]
