# Generated by Django 4.1 on 2022-10-02 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserBlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, default='pro2.jpeg', null=True, upload_to='avatares'),
        ),
    ]
