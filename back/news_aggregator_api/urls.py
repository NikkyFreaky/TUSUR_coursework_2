from django.urls import path
from . import views

urlpatterns = [
    # Финальные
    path('news/', views.get_all_news, name='all_news'),
    path('news/<str:category>/', views.get_news, name='get_news_by_category'),
    
    # Для тестов и проверки
    path('', views.default),
    path('scrape/', views.scrape, name='scrape'),
    path('get_news_by_country/', views.get_news_by_country, name='get_news_by_country'),  # эндпоинт для вывода новостей
]
