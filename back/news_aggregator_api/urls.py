from django.urls import path
from . import views

urlpatterns = [
    # Финальные
    path('news/', views.get_all_news, name='all_news'),
    path('news/category/<str:category>/', views.get_news_by_category, name='get_news_by_category'),
    path('news/country/<str:country>/', views.get_news_by_country, name='get_news_by_country'),
    path('news/date/<str:date>/', views.get_news_by_date, name='get_news_by_date'),
   
    # Для тестов и проверки
    path('', views.default),
    path('scrape/', views.scrape, name='scrape'),
    path('get_news_for_country/', views.get_news_for_country, name='get_news_for_country'),  # эндпоинт для вывода новостей

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('add_news_to_category/', views.add_news_to_category, name='add_news_to_category'),
    path('create_user_category/', views.create_user_category, name='create_user_category'),

]
