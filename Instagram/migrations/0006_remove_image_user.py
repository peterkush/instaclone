# Generated by Django 3.1.3 on 2020-11-21 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Instagram', '0005_auto_20201121_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='user',
        ),
    ]
