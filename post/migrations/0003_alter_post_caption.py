# Generated by Django 3.2.17 on 2023-04-10 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20230209_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(max_length=10000, verbose_name='Caption'),
        ),
    ]
