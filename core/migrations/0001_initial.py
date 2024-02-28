# Generated by Django 4.1.7 on 2024-02-28 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('username', models.CharField(max_length=10, verbose_name='Username')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('gender', models.BinaryField(choices=[('M', 'Male'), ('F', 'Female')])),
            ],
        ),
    ]