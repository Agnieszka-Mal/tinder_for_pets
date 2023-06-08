# Generated by Django 4.2.1 on 2023-06-02 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetsProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pets_name', models.CharField(max_length=30)),
                ('type_of_pet', models.CharField(choices=[('kot', 'kot'), ('pies', 'pies')])),
                ('breed', models.CharField(max_length=128)),
                ('sex', models.CharField(choices=[('female', 'female'), ('male', 'male')])),
                ('age', models.DecimalField(decimal_places=1, max_digits=3)),
                ('description', models.TextField()),
                ('activity', models.IntegerField(choices=[(1, 'spacery'), (2, 'bieganie'), (3, 'wędrówki'), (4, 'spotkania'), (5, 'sport'), (6, 'słodkie lenistwo'), (7, 'dobre jedzonko')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('profile_foto', models.ImageField(upload_to='pets_profile')),
                ('tinder_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.tinderuser')),
            ],
        ),
        migrations.CreateModel(
            name='PetsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(upload_to='images')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.tinderuser')),
            ],
            options={
                'ordering': ('created_at',),
                'abstract': False,
            },
        ),
    ]