# Generated by Django 3.1.7 on 2021-09-15 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salesforce', '0003_remove_account_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
    ]
