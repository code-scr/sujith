# Generated by Django 3.2.17 on 2023-03-06 03:58

from django.db import migrations, models
import userauths.models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0002_auto_20230225_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', null=True, upload_to=userauths.models.user_directory_path),
        ),
    ]
