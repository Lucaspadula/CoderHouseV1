# Generated by Django 4.1 on 2022-10-03 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserBlog', '0003_user_delete_avatar'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]