
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_id', models.IntegerField(null=True, unique=True)),
                ('candidate_name', models.CharField(max_length=50)),
                ('party_name', models.CharField(max_length=128)),
                ('candidate_publickey', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_no', models.CharField(max_length=50)),
                ('unique_hash', models.CharField(max_length=128)),
                ('voter_publickey', models.CharField(max_length=128)),
                ('isverify', models.BooleanField()),

            ],
        ),
    ]
