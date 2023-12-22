from django.db import models
from django.conf import settings

from django.contrib.auth.models import User, Group
from django.contrib.auth.models import AbstractUser

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


class UserProfile(AbstractUser):
    # Поля
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group, blank=True, help_text='Системный доступ пользователя')
    registration_date = models.DateField(auto_now_add=True, help_text='Дата регистрации пользователя')
    last_login = models.DateField(auto_now=True, help_text='Дата последнего входа пользователя')

    # Обязательные поля
    REQUIRED_FIELDS = ['groups', 'registration_date']

    '''
     # Метаданные
    class Meta:
        ordering = ["-user.username", "-last_login"]
    '''

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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_category_name = models.CharField(max_length=30, help_text='Название пользовательской категории')

    # Метаданные
    class Meta:
        ordering = ["user_category_name"]
    
    # Методы
    def __str__(self):
        return f"{self.user.username} (User categories: {self.user_category_name})"
    

class Category(models.Model):
    # Категории
    POLITICAL = 'Политика'
    ECONOMY = 'Экономика'
    TECHNOLOGY = 'Технологии'
    SPORT = 'Спорт'
    HEALTH_SCIENCE = 'Наука и Здоровье'
    ENTERTAINMENT = 'Развлечения'
    CRIME = 'Криминал'

    CATEGORY_CHOICES = [
        (POLITICAL, 'Политика'),
        (ECONOMY, 'Экономика'),
        (TECHNOLOGY, 'Технологии'),
        (SPORT, 'Спорт'),
        (HEALTH_SCIENCE, 'Наука и Здоровье'),
        (ENTERTAINMENT, 'Развлечения'),
        (CRIME, 'Криминал'),
    ]

    # Поля
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50, choices=CATEGORY_CHOICES, help_text='Название категории')

    # Методы
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
    source_name = models.CharField(max_length=50, help_text='Название источника', blank=True)
    source_link = models.CharField(max_length=100, help_text='Ссылка на источник')

    # Методы
    def __str__(self):
        return f"{self.source_name} (Source link: {self.source_link})"
    

class News(models.Model):
    # Поля
    news_id = models.AutoField(primary_key=True)
    source = models.ForeignKey('Source', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, help_text='Название новости')
    description = models.TextField(help_text='Полный текст новости')
    event_date = models.DateField(null=True, help_text='Дата произошедшего события')
    publication_date = models.DateField(auto_now=True, help_text='Дата публикации')
    categories = models.ManyToManyField(Category, related_name='news', blank=True)
    countries = models.ManyToManyField(Country, related_name='news', blank=True)
    regions = models.ManyToManyField(Region, related_name='news', blank=True)
    cities = models.ManyToManyField(City, related_name='news', blank=True)

    # Метаданные
    class Meta:
        ordering = ["title", "-publication_date"]

    # Методы
    def __str__(self):
        return f"{self.title} (Publication date: {self.publication_date})"
    

class Asset(models.Model):
    # Поля
    asset_id = models.AutoField(primary_key=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    images = models.ImageField(null=True, blank=True, upload_to='assets/images/', help_text='Изображения приклепленные к новости')
    videos = models.FileField(null=True, blank=True, upload_to='assets/images/', help_text='Видео приклепленные к новости')


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
    famous_date = models.DateField(auto_now=True, help_text='Известная дата')

    # Методы
    def __str__(self):
        return f"{self.category.category_name} (Famous date: {self.famous_date})"