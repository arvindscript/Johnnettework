# Generated by Django 5.1.5 on 2025-02-05 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portal_App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='Confirm_password',
            new_name='username',
        ),
    ]
