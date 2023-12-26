from django.http import JsonResponse
from ..models import News
import datetime

def get_news(request, category=None, country=None, date=None):
    success = True
    message = 'Запрос успешно выполнен'
    news_list = []

    try:
        # Фильтр по категории
        if category:
            all_news = News.objects.filter(categories__category_name=category)

        # Фильтр по стране
        elif country:
            all_news = News.objects.filter(countries__country_name=country)

        # Фильтр по дате
        elif date:
            # Если фильтр по дате - 'past 7 days'
            if isinstance(date, datetime.timedelta):
                start_date = datetime.date.today() - date
                all_news = News.objects.filter(event_date__gte=start_date)
            # Если фильтр по дате - 'today', 'this month', 'this year'
            else:
                all_news = News.objects.filter(event_date__gte=date)
                
        # В противном случае получаем все новости
        else:
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
                'assets': asset_info,
            })
    except Exception as e:
        success = False
        message = f'Ошибка при обработке запроса: {str(e)}'

    return JsonResponse({'success': success, 'message': message, 'news': news_list})