# Generated by Django 2.2.1 on 2020-02-08 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0004_auto_20200208_2144'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserVerification',
        ),
    ]