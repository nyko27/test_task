# Generated by Django 5.0.6 on 2024-05-10 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set(),
        ),
    ]