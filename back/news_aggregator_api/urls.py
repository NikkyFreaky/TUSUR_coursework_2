from django.urls import path
from . import views

urlpatterns = [
    # Финальные
    path('', views.default, name='default'),
    path('parse/<str:country>/', views.parse_news_by_country, name='parse_news_by_country'),

    path('news/', views.get_all_news, name='all_news'),
    path('news/category/<str:category>/', views.get_news_by_category, name='get_news_by_category'),
    path('news/country/<str:country>/', views.get_news_by_country, name='get_news_by_country'),
    path('news/date/<str:date>/', views.get_news_by_date, name='get_news_by_date'),
    path('news/search/', views.news_search_by_keywords, name='news_search_by_keywords'),
   
    # Для тестов и проверки
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('get_user_data/', views.get_user_data, name='get_user_data'),

    path('add_news_to_category/', views.add_news_to_category, name='add_news_to_category'),
    path('create_user_category/', views.create_user_category, name='create_user_category'),
    path('get_user_category/', views.get_user_categories, name='get_user_categories'),
    path('news_user_category/', views.get_news_from_user_categories, name='news_user_category'),
    path('delete_category/', views.del_user_categories, name='delete_category'),
    path('delete_news/', views.del_news_from_user_category, name='delete_news'),

]
