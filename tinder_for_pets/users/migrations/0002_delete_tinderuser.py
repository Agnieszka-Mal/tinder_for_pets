# Generated by Django 4.2.1 on 2023-06-03 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets_profile', '0002_alter_petsimage_owner_alter_petsprofile_tinder_user'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TinderUser',
        ),
    ]