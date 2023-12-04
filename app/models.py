from django.db import models

class System(models.Model):
    system_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    version = models.CharField(max_length=10)
    last_update = models.DateField()

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    user_first_name = models.CharField(max_length=50)
    user_last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    role = models.CharField(max_length=20)
    registration_date = models.DateField()
    last_login = models.DateField()

class UserCategory(models.Model):
    user_category_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_category_name = models.CharField(max_length=30)

class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    source = models.ForeignKey('Source', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    event_date = models.DateField()
    publication_date = models.DateField()

class Source(models.Model):
    source_id = models.AutoField(primary_key=True)
    source_name = models.CharField(max_length=50)
    source_link = models.CharField(max_length=100)

class Asset(models.Model):
    asset_id = models.AutoField(primary_key=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    images = models.BinaryField(null=True, blank=True)
    videos = models.BinaryField(null=True, blank=True)

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)

class Celebrity(models.Model):
    celebrity_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    celebrity_first_name = models.CharField(max_length=50)
    celebrity_last_name = models.CharField(max_length=50)

class FamousEvent(models.Model):
    famous_event_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    famous_event_name = models.CharField(max_length=50)

class FamousDate(models.Model):
    famous_date_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    famous_date = models.DateField()

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=30)

class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region_name = models.CharField(max_length=50)

class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50)