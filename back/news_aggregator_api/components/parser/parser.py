import requests
from ...models import News, Source, Asset, Category, Country
from datetime import datetime
from django.utils import timezone

def parse_news(country):
    api_key = '238131f7f6664e22b6d625ac06847c72'
    categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
    total_news_saved = 0  # Добавим счетчик сохраненных новостей
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
            print(f'Не найдена страна {country}')
            return

        response = requests.get(url, params=params)

        if response.status_code == 200:
            news_data = response.json()

            for article in news_data.get('articles', []):
                title = article.get('title', '')
                # Проверяем, содержится ли '[Removed]' в заголовке новости
                if '[Removed]' in title:
                    print(f"Пропущена новость с заголовком '{title}' (содержит '[Removed]')")
                    continue  # Пропускаем текущую итерацию цикла

                link = article.get('url', '')
                image_src = article.get('urlToImage', '')
                source_name = article.get('source', {}).get('name', '')
                content = article.get('content', '')
                published_at_string = article.get('publishedAt', '')

                # Преобразуем строку с датой в объект datetime с часовым поясом UTC
                published_at_datetime = datetime.strptime(published_at_string, "%Y-%m-%dT%H:%M:%SZ")
                published_at_datetime = timezone.make_aware(published_at_datetime, timezone.utc)

                # Создаем и сохраняем объект Source
                source, created = Source.objects.get_or_create(source_name=source_name, source_link=link)

                country_obj, country_created = Country.objects.get_or_create(country_name=country)

                # Создаем и сохраняем объект News только если его еще нет в базе
                news, created = News.objects.get_or_create(
                    title=title,
                    source=source,
                    description=content,
                    publication_date=published_at_datetime,
                    event_date=published_at_datetime.date(),
                    defaults={'title': title, 'source': source, 'publication_date': published_at_datetime}
                )

                # Если новость уже существует, created будет равен False, и вы можете, например, вывести сообщение
                if not created:
                    print(f"Новость с заголовком '{title}' уже существует в базе данных.")
                else:
                    total_news_saved += 1  # Увеличиваем счетчик сохраненных новостей

                # Создаем и сохраняем объект Asset
                asset = Asset.objects.create(images=image_src, news=news)

                # Присваиваем категорию новости
                category_obj, created = Category.objects.get_or_create(category_name=category)
                news.categories.add(category_obj)

                news.countries.add(country_obj)

    print(f"Всего сохранено {total_news_saved} новостей в базу данных.")