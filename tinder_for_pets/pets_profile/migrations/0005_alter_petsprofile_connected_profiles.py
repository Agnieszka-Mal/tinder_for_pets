# Generated by Django 4.2.1 on 2023-06-08 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_profile', '0004_petsprofile_connected_profiles_petsprofile_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petsprofile',
            name='connected_profiles',
            field=models.ManyToManyField(blank=True, null=True, to='pets_profile.petsprofile'),
        ),
    ]
