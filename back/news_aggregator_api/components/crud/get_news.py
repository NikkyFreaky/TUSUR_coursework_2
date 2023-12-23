from django.http import JsonResponse
from ...models import News

def get_news(request, category=None):
    success = True
    message = 'Запрос успешно выполнен'
    news_list = []

    try:
        if category:
            # Если предоставлена категория, фильтруем новости по этой категории
            all_news = News.objects.filter(categories__category_name=category)
        else:
            # Иначе получаем все новости
            all_news = News.objects.all()

        for news in all_news:
            assets = news.asset_set.all()
            asset_info = {
                'images': assets[0].images if assets else None,
                'videos': assets[0].videos if assets else None,
            }

            news_list.append({
                'source': {
                    'name': news.source.source_name,
                    'link': news.source.source_link,
                },
                'title': news.title,
                'description': news.description,
                'event_date': news.event_date.isoformat() if news.event_date else None,
                'publication_date': news.publication_date.isoformat(),
                'categories': [category.category_name for category in news.categories.all()],
                'countries': [country.country_name for country in news.countries.all()],
                'asset': asset_info,
            })
    except Exception as e:
        success = False
        message = f'Ошибка при обработке запроса: {str(e)}'

    return JsonResponse({'success': success, 'message': message, 'news': news_list})
