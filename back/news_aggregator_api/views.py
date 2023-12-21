from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup as BSoup
from .models import News, Source, Asset
import certifi
from django.template.defaultfilters import truncatechars

# Create your views here.


def scrape(request):  # эта штука парсит, надо здесь там всякие категории передавать, дескрипшн еще и опционально страны и т.д.
    api_key = '238131f7f6664e22b6d625ac06847c72'
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'us',  # Укажите страну, из которой хотите получить новости
        'apiKey': api_key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        news_data = response.json()

        for article in news_data.get('articles', []):
            title = truncatechars(article.get('title', ''), 90)
            link = truncatechars(article.get('url', ''), 90)
            image_src = truncatechars(article.get('urlToImage', ''), 90)

            # Создаем и сохраняем объект Source
            source_name = article.get('source', {}).get('name', '')



            source, created = Source.objects.get_or_create(source_name=source_name, source_link=link)

            # Создаем и сохраняем объект News
            news = News.objects.create(title=title, source=source)

            # Создаем и сохраняем объект Asset
            asset = Asset.objects.create(images=image_src, news=news)


        return redirect("../")
    else:
        print(f"Failed to fetch news. Status code: {response.status_code}")
        return redirect("../")


def default(request):
    return render(request, 'default.html')
