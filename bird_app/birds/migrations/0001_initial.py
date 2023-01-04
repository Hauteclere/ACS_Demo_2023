# Generated by Django 4.1.5 on 2023-01-04 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BirdSighting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unknown')], max_length=1)),
                ('age', models.CharField(choices=[('E', 'Egg'), ('H', 'Hatchling'), ('J', 'Juvenile'), ('A', 'Adult')], max_length=1)),
                ('location', models.CharField(max_length=100)),
                ('activity', models.CharField(max_length=100)),
                ('spotter', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
