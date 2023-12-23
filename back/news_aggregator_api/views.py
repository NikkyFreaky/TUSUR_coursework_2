from django.shortcuts import render, redirect
from .components.parser import parse_news
from .models import News, Country
from django.http import JsonResponse
# Create your views here.


def get_news_by_country(request):  # сам эндпоинт

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