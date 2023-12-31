# Generated by Django 4.2.7 on 2023-12-24 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(help_text='Название категории', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(help_text='Название города', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.AutoField(primary_key=True, serialize=False)),
                ('country_name', models.CharField(help_text='Название страны', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('source_id', models.AutoField(primary_key=True, serialize=False)),
                ('source_name', models.CharField(help_text='Название источника', max_length=500)),
                ('source_link', models.CharField(help_text='Ссылка на источник', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('system_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Название системы', max_length=10)),
                ('version', models.CharField(help_text='Версия системы', max_length=10)),
                ('last_update', models.DateField(auto_now=True, help_text='Дата последнего обновления системы')),
            ],
            options={
                'ordering': ['-last_update'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateField(auto_now_add=True, help_text='Дата регистрации пользователя')),
                ('last_login', models.DateField(auto_now=True, help_text='Дата последнего входа пользователя')),
                ('groups', models.ManyToManyField(blank=True, help_text='Системный доступ пользователя', to='auth.group')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_aggregator_api.system')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserCategory',
            fields=[
                ('user_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_category_name', models.CharField(help_text='Название пользовательской категории', max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user_category_name'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region_id', models.AutoField(primary_key=True, serialize=False)),
                ('region_name', models.CharField(help_text='Название региона', max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_aggregator_api.country')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='Название новости', max_length=50000)),
                ('description', models.TextField(blank=True, help_text='Полный текст новости', null=True)),
                ('event_date', models.DateField(help_text='Дата произошедшего события', null=True)),
                ('publication_date', models.DateTimeField(help_text='Дата публикации')),
                ('categories', models.ManyToManyField(blank=True, related_name='news', to='news_aggregator_api.category')),
                ('cities', models.ManyToManyField(blank=True, related_name='news', to='news_aggregator_api.city')),
                ('countries', models.ManyToManyField(blank=True, related_name='news', to='news_aggregator_api.country')),
                ('regions', models.ManyToManyField(blank=True, related_name='news', to='news_aggregator_api.region')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_aggregator_api.source')),
            ],
            options={
                'ordering': ['title', '-publication_date'],
            },
        ),
        migrations.CreateModel(
            name='FamousEvent',
            fields=[
                ('famous_event_id', models.AutoField(primary_key=True, serialize=False)),
                ('famous_event_name', models.CharField(help_text='Название известного события', max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_aggregator_api.category')),
            ],
        ),
        migrations.CreateModel(
            name='FamousDate',
            fields=[
                ('famous_date_id', models.AutoField(primary_key=True, serialize=False)),
                ('famous_date', models.DateField(auto_now=True, help_text='Известная дата')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_aggregator_api.category')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_aggregator_api.region'),
        ),
        migrations.CreateModel(
            name='Celebrity',
            fields=[
                ('celebrity_id', models.AutoField(primary_key=True, serialize=False)),
                ('celebrity_first_name', models.CharField(help_text='Имя известного человека', max_length=50)),
                ('celebrity_last_name', models.CharField(help_text='Фамилия известного человека', max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_aggregator_api.category')),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('asset_id', models.AutoField(primary_key=True, serialize=False)),
                ('images', models.CharField(blank=True, help_text='Изображения приклепленные к новости', max_length=1000, null=True)),
                ('videos', models.CharField(blank=True, help_text='Видео приклепленные к новости', max_length=1000, null=True)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_aggregator_api.news')),
            ],
        ),
    ]
