from django.urls import path
from . import views

urlpatterns = [
    path('scrape/', views.scrape, name='scrape'),
    path('', views.default),
    path('get_news_by_country/', views.get_news_by_country, name='get_news_by_country'),  # эндпоинт для вывода новостей
]
