# Generated by Django 5.1.2 on 2024-10-28 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_userprofile_delete_glass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='contact_no',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='role',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]
