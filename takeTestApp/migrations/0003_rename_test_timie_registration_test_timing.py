# Generated by Django 4.2.4 on 2023-08-12 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('takeTestApp', '0002_alter_testcenter_endtiming_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='test_timie',
            new_name='test_timing',
        ),
    ]