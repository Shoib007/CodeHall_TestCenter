# Generated by Django 4.2.4 on 2023-08-12 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location_lat', models.FloatField()),
                ('location_long', models.FloatField()),
                ('startTiming', models.DateTimeField()),
                ('endTiming', models.DateTimeField()),
                ('totalSeats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('test_date', models.DateField()),
                ('test_timie', models.TimeField()),
                ('test_duration', models.DurationField()),
                ('testCenter', models.ManyToManyField(to='takeTestApp.testcenter')),
            ],
        ),
    ]