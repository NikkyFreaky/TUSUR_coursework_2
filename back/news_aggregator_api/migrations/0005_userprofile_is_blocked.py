# Generated by Django 4.2.7 on 2023-12-26 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_aggregator_api', '0004_alter_source_source_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_blocked',
            field=models.BooleanField(default=False),
        ),
    ]
