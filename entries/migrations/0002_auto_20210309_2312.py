# Generated by Django 3.1.7 on 2021-03-09 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='entry_data',
            new_name='entry_date',
        ),
    ]