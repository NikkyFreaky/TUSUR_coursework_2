from django.shortcuts import render, redirect
from .components.parser.parser import parse_news
from .components.crud.get_news import get_news
from .models import News, Country
from django.http import JsonResponse
import datetime

# Create your views here.

# Возвращает все новости
def get_all_news(request):
    return get_news(request)

# Возвращает новости по категории
def get_news_by_category(request, category):
    return get_news(request, category=category)

# Возвращает новости по стране
def get_news_by_country(request, country):
    return get_news(request, country=country)

# Возвращает новости по дате
def get_news_by_date(request, date):
    today = datetime.date.today()
    
    if date == "today":
        date_filter = today
    elif date == "past7days":
        date_filter = today - datetime.timedelta(days=7)
    elif date == "month":
        first_day_of_month = today.replace(day=1)
        date_filter = first_day_of_month
    elif date == "year":
        first_day_of_year = today.replace(month=1, day=1)
        date_filter = first_day_of_year
    else:
        return JsonResponse({'success': False, 'message': 'Неправильный формат даты'})

    return get_news(request, date=date_filter)


def get_news_for_country(request):  # сам эндпоинт

    if request.method == 'GET':
        country_name = request.GET.get('country_name')
        try:
            parse_news(country_name)
            country = Country.objects.get(country_name=country_name)
            news_by_country = News.objects.filter(countries=country)
            news_data = [
                {
                    'title': news.title,
                    'description': news.description,
                    'event_date': news.event_date,
                    'publication_date': news.publication_date,
                    # добавить ругие поля которые надо выдать на фронт
                }
                for news in news_by_country
            ]
            return JsonResponse({'news': news_data})
        except Country.DoesNotExist:
            return JsonResponse({'error': 'Страна не найдена'}, status=404)
    return redirect("../")


def scrape(request):
    if request.method == 'GET':
        country_name = request.GET.get('country_name')
        parse_news(country_name)
    return redirect("../")


def default(request):
    return render(request, 'default.html')