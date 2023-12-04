# Generated by Django 4.2.6 on 2023-12-04 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.AutoField(primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('source_id', models.AutoField(primary_key=True, serialize=False)),
                ('source_name', models.CharField(max_length=50)),
                ('source_link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('system_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('version', models.CharField(max_length=10)),
                ('last_update', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('user_first_name', models.CharField(max_length=50)),
                ('user_last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=20)),
                ('registration_date', models.DateField()),
                ('last_login', models.DateField()),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.system')),
            ],
        ),
        migrations.CreateModel(
            name='UserCategory',
            fields=[
                ('user_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_category_name', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region_id', models.AutoField(primary_key=True, serialize=False)),
                ('region_name', models.CharField(max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.country')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('event_date', models.DateField()),
                ('publication_date', models.DateField()),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.source')),
            ],
        ),
        migrations.CreateModel(
            name='FamousEvent',
            fields=[
                ('famous_event_id', models.AutoField(primary_key=True, serialize=False)),
                ('famous_event_name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='FamousDate',
            fields=[
                ('famous_date_id', models.AutoField(primary_key=True, serialize=False)),
                ('famous_date', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=50)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.region')),
            ],
        ),
        migrations.CreateModel(
            name='Celebrity',
            fields=[
                ('celebrity_id', models.AutoField(primary_key=True, serialize=False)),
                ('celebrity_first_name', models.CharField(max_length=50)),
                ('celebrity_last_name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('asset_id', models.AutoField(primary_key=True, serialize=False)),
                ('images', models.BinaryField(blank=True, null=True)),
                ('videos', models.BinaryField(blank=True, null=True)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.news')),
            ],
        ),
    ]
