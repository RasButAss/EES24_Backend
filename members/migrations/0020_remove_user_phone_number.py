# Generated by Django 5.0 on 2024-01-30 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0019_user_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
    ]