import requests
from datetime import datetime
from django.core.management.base import BaseCommand
from ...models import News, Source

class Command(BaseCommand):
    help = 'Fetch and store news from an external API'

    def handle(self, *args, **options):
        api_key = '238131f7f6664e22b6d625ac06847c72'
        api_url = 'https://newsapi.org/v2/top-headlines'
        params = {
            'country': 'ru',
            'apiKey': api_key,
        }

        try:
            response = requests.get(api_url, params=params)
            response.raise_for_status()  # Raise an HTTPError for bad responses

            news_data = response.json().get('articles', [])

            for article in news_data:
                source_data = article.get('source', {})
                source_id = source_data.get('id')
                source_name = source_data.get('name')
                
                if source_id and source_name:
                    source, created = Source.objects.get_or_create(
                        source_id=source_id,
                        defaults={'source_name': source_name}
                    )

                    News.objects.create(
                        source=source,
                        title=article.get('title'),
                        description=article.get('description'),
                        event_date=datetime.strptime(article.get('publishedAt'), '%Y-%m-%dT%H:%M:%SZ'),
                        publication_date=datetime.now(),
                    )

            self.stdout.write(self.style.SUCCESS('Successfully fetched and stored news'))

        except requests.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Error fetching news: {e}'))