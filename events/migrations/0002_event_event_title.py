# Generated by Django 4.0.4 on 2022-06-05 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_title',
            field=models.CharField(default='default title', max_length=30),
        ),
    ]
