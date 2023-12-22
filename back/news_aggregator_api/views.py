from django.shortcuts import render, redirect
import requests
from .models import News, Source, Asset, Category
from datetime import datetime
from django.utils import timezone


# Create your views here.

# эта штука парсит, надо здесь там всякие категории передавать, дескрипшн еще и опционально страны и т.д.

def scrape(request):
    api_key = '238131f7f6664e22b6d625ac06847c72'
    categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']

    for category in categories:
        url = 'https://newsapi.org/v2/top-headlines'
        params = {
            'country': 'us',
            'category': category,
            'apiKey': api_key
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            news_data = response.json()

            for article in news_data.get('articles', []):
                title = article.get('title', '')
                link = article.get('url', '')
                image_src = article.get('urlToImage', '')
                source_name = article.get('source', {}).get('name', '')
                content = article.get('content', '')
                published_at_datetime = article.get('publishedAt', '')
                published_at_date = article.get('publishedAt', '')

                # Преобразуем строку с датой в объект datetime
                published_at_datetime = datetime.strptime(published_at_datetime, "%Y-%m-%dT%H:%M:%SZ")
                published_at_date = datetime.strptime(published_at_date, "%Y-%m-%dT%H:%M:%SZ").date()

                # Создаем и сохраняем объект Source
                source, created = Source.objects.get_or_create(source_name=source_name, source_link=link)

                # Создаем и сохраняем объект News
                news = News.objects.create(
                    title=title,
                    source=source,
                    description=content,
                    publication_date=published_at_datetime,
                    event_date=published_at_date
                )

                # Создаем и сохраняем объект Asset
                asset = Asset.objects.create(images=image_src, news=news)

                # Присваиваем категорию новости
                category_obj, created = Category.objects.get_or_create(category_name=category)
                news.categories.add(category_obj)

            # Не используем return внутри цикла
    return redirect("../")


def default(request):
    return render(request, 'default.html')