# Generated by Django 4.2.1 on 2023-06-08 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_profile', '0005_alter_petsprofile_connected_profiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petsprofile',
            name='connected_profiles',
            field=models.ManyToManyField(blank=True, to='pets_profile.petsprofile'),
        ),
    ]
