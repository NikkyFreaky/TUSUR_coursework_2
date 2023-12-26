from django.db.models import Q
from django.http import JsonResponse
from ..models import News

def news_search(request):
    query = request.GET.get('q', '')
    if not query:
        return JsonResponse({'success': False, 'message': 'Пустой запрос'})

    results = News.objects.filter(Q(title__icontains=query))

    news_list = []
    for news in results:
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

    return JsonResponse({'success': True, 'results': news_list})
