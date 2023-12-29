from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class System(models.Model):
    # Поля
    system_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, help_text='Название системы')
    version = models.CharField(max_length=10, help_text='Версия системы')
    last_update = models.DateField(auto_now=True, help_text='Дата последнего обновления системы')

    # Метаданные
    class Meta:
        ordering = ["-last_update"]

    # Методы
    def __str__(self):
        return f"{self.name} (Last update: {self.last_update})"


class UserProfile(models.Model):
   # Поля
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group, blank=True, help_text='Системный доступ пользователя')
    registration_date = models.DateField(auto_now_add=True, help_text='Дата регистрации пользователя')
    last_login = models.DateField(auto_now=True, help_text='Дата последнего входа пользователя')
    is_blocked = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)
     # Методы

    def __str__(self):
        if self.user.groups.filter(name='Администратор').exists():
            return f"Администратор - {self.user.username} (Last login: {self.last_login})"
        elif self.user.groups.filter(name='Пользователь').exists():
            return f"Пользователь - {self.user.username} (Last login: {self.last_login})"
        else:
            return f"Другая группа - {self.user.username} (Last login: {self.last_login})"


class UserCategory(models.Model):
    # Поля
    user_category_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_category_name = models.CharField(max_length=30, help_text='Название пользовательской категории')
    news = models.ManyToManyField('News', related_name='user_categories', blank=True)

    # Метаданные
    class Meta:
        ordering = ["user_category_name"]
    
    # Методы
    def __str__(self):
        return f"{self.user.username} (User categories: {self.user_category_name})"
    

class Category(models.Model):
    # Поля
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50, help_text='Название категории')

    # Методы
    @classmethod
    def get_or_create_by_name(cls, name):
        category, created = cls.objects.get_or_create(category_name=name)
        return category

    def __str__(self):
        return self.category_name
    

class Country(models.Model):
    # Поля
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=30, help_text='Название страны')

    # Методы
    def __str__(self):
        return self.country_name

class Region(models.Model):
    # Поля
    region_id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region_name = models.CharField(max_length=50, help_text='Название региона')

    # Методы
    def __str__(self):
        return self.region_name

class City(models.Model):
    # Поля
    city_id = models.AutoField(primary_key=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50, help_text='Название города')

    # Методы
    def __str__(self):
        return self.city_name
    

class Source(models.Model):
    # Поля
    source_id = models.AutoField(primary_key=True)
    source_name = models.CharField(max_length=500, help_text='Название источника')
    source_link = models.CharField(max_length=2500, help_text='Ссылка на источник')

    # Методы
    def __str__(self):
        return f"{self.source_name} (Source link: {self.source_link})"
    

class News(models.Model):
    # Поля
    news_id = models.AutoField(primary_key=True)
    source = models.ForeignKey('Source', on_delete=models.CASCADE)
    title = models.CharField(max_length=50000, help_text='Название новости')
    description = models.TextField(blank=True, null=True, help_text='Полный текст новости')
    event_date = models.DateField(help_text='Дата произошедшего события', null=True)
    publication_date = models.DateTimeField(help_text='Дата публикации')
    categories = models.ManyToManyField(Category, related_name='news', blank=True)
    countries = models.ManyToManyField(Country, related_name='news', blank=True)
    regions = models.ManyToManyField(Region, related_name='news', blank=True)
    cities = models.ManyToManyField(City, related_name='news', blank=True)

    # Метаданные
    class Meta:
        ordering = ["-publication_date", "title"]

    # Методы
    def __str__(self):
        return f"{self.title} (Publication date: {self.publication_date})"
    

class Asset(models.Model):
    # Поля
    asset_id = models.AutoField(primary_key=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    images = models.CharField(max_length=1000, blank=True, null=True, help_text='Изображения приклепленные к новости')
    videos = models.CharField(max_length=1000, blank=True, null=True, help_text='Видео приклепленные к новости')


class Celebrity(models.Model):
    # Поля
    celebrity_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    celebrity_first_name = models.CharField(max_length=50, help_text='Имя известного человека')
    celebrity_last_name = models.CharField(max_length=50, help_text='Фамилия известного человека')

    # Методы
    def __str__(self):
        return f"{self.category.category_name} (Celebrity name: {self.celebrity_first_name} {self.celebrity_last_name})"
    

class FamousEvent(models.Model):
    # Поля
    famous_event_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    famous_event_name = models.CharField(max_length=50, help_text='Название известного события')

    # Методы
    def __str__(self):
        return f"{self.category.category_name} (Famous event name: {self.famous_event_name})"
    
class FamousDate(models.Model):
    # Поля
    famous_date_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    famous_date = models.DateField(help_text='Известная дата')

    # Методы
    def __str__(self):
        return f"{self.category.category_name} (Famous date: {self.famous_date})"