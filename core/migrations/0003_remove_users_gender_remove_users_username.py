# Generated by Django 4.1.7 on 2024-02-28 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_users_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='users',
            name='username',
        ),
    ]
