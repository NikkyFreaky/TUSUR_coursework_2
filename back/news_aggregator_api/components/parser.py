import requests
from ..models import News, Source, Asset, Category, Country
from datetime import datetime
from django.utils import timezone
from django.http import JsonResponse

def parse_news(country):
    api_key = '238131f7f6664e22b6d625ac06847c72'
    categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
    total_news_saved = 0
    countries = ['ae', 'ar', 'at', 'au', 'be', 'bg', 'br', 'ca', 'ch', 'cn', 'co', 'cu', 'cz', 'de', 'eg', 'fr', 'gb',
                 'gr', 'hk', 'hu', 'id', 'ie', 'il', 'in', 'it', 'jp', 'kr', 'lt', 'lv', 'ma', 'mx', 'my', 'ng', 'nl',
                 'no', 'nz', 'ph', 'pl', 'pt', 'ro', 'rs', 'ru', 'sa', 'se', 'sg', 'si', 'sk', 'th', 'tr', 'tw', 'ua',
                 'us', 've', 'za']

    for category in categories:
        url = 'https://newsapi.org/v2/top-headlines'
        if country in countries:
            params = {
                'country': country,
                'category': category,
                'apiKey': api_key
            }
        else:
            params = {
                'category': category,
                'apiKey': api_key
            }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            news_data = response.json()

            if 'status' in news_data and news_data['status'] == 'error':
                return JsonResponse({'error': news_data.get('message', 'Ошибка при запросе данных')}, status=500)

            for article in news_data.get('articles', []):
                title = article.get('title', '')

                # Проверяем, содержится ли '[Removed]' в заголовке новости
                if '[Removed]' in title:
                    print(f"Пропущена новость с заголовком '{title}' (содержит '[Removed]')")
                    continue

                link = article.get('url', '')
                image_src = article.get('urlToImage', '')
                source_name = article.get('source', {}).get('name', '')
                description = article.get('description', '')
                published_at_string = article.get('publishedAt', '')

                # Преобразуем строку с датой в объект datetime с часовым поясом UTC
                published_at_datetime = datetime.strptime(published_at_string, "%Y-%m-%dT%H:%M:%SZ")
                published_at_datetime = timezone.make_aware(published_at_datetime, timezone=timezone.utc)

                # Создаем и сохраняем объект Source
                source, created = Source.objects.get_or_create(source_name=source_name, source_link=link)

                country_obj, country_created = Country.objects.get_or_create(country_name=country)

                # Создаем и сохраняем объект News только если его еще нет в базе
                news, created = News.objects.get_or_create(
                    title=title,
                    source=source,
                    description=description,
                    publication_date=published_at_datetime,
                    event_date=published_at_datetime.date(),
                    defaults={'title': title, 'source': source, 'publication_date': published_at_datetime}
                )

                # Если новость уже существует, created будет равен False
                if not created:
                    print(f"Новость с заголовком '{title}' уже существует в базе данных.")
                else:
                    total_news_saved += 1

                # Создаем и сохраняем объект Asset
                asset = Asset.objects.create(images=image_src, news=news)

                # Присваиваем категорию новости
                category_obj, created = Category.objects.get_or_create(category_name=category)
                news.categories.add(category_obj)

                news.countries.add(country_obj)

    if total_news_saved > 0:
        return {'success': True, 'message': f'Всего сохранено {total_news_saved} новостей в базу данных.'}
    else:
        return {'success': False, 'message': 'Новые новости отсутствуют или произошла ошибка при парсинге.'}