# Generated by Django 2.2.1 on 2020-11-03 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20201103_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=44, unique=True),
        ),
    ]
