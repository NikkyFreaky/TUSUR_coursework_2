# Generated by Django 4.2.7 on 2023-12-24 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_aggregator_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercategory',
            name='news',
            field=models.ManyToManyField(blank=True, related_name='user_categories', to='news_aggregator_api.news'),
        ),
    ]
