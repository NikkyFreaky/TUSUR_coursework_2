from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .components.parser import parse_news
from .components.get_news import get_news
from .components.search_news import news_search
from .models import UserProfile, Group, System, UserCategory, News
from django.http import JsonResponse
import datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ExtendedUserCreationForm, EmailAuthenticationForm, UserCategoryForm, AddNewsToCategoryForm
from django.contrib.auth import authenticate, login as auth_login, logout
import json


# Create your views here.

# Возвращает все новости
def default(request):
    return render(request, 'default.html')


# Парсим новости по стране
def parse_news_by_country(request, country):
    response = parse_news(country)
    return JsonResponse(response, safe=False)


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


# Поиск новостей по ключевым словам
@csrf_exempt
def news_search_by_keywords(request):
    data = json.loads(request.body.decode('utf-8'))
    search_value = data.get('searchValue')
    return news_search(request, search_value)


#  ниже простарнство для создания новых функций

@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            # Получаем данные из тела запроса
            data = json.loads(request.body.decode('utf-8'))

            # Создаем форму с данными из запроса
            form = ExtendedUserCreationForm(data)

            if form.is_valid():
                # Создаем пользователя
                user = form.save()

                # Добавляем пользователя в группу "Пользователь"
                user_group, created = Group.objects.get_or_create(name='Пользователь')
                user.groups.add(user_group)

                # Копируем права из группы в пользователя
                for permission in user_group.permissions.all():
                    user.user_permissions.add(permission)

                system, created = System.objects.get_or_create(name='alfa test', version='0.0.1')

                # Создаем профиль пользователя
                UserProfile.objects.create(user=user, system=system)

                auth_login(request, user)
                django_session = Session.objects.get(session_key=request.session.session_key)
                # Пример успешного ответа
                response_data = {'status': 'success',
                                 'message': 'Registration successful',
                                 'sessionid': django_session.session_key,
                                 'session_expire_at': django_session.expire_date.timestamp(), }
                return JsonResponse(response_data)
            else:
                # Пример ответа с ошибками формы
                print(form.errors)
                if 'This password is too common.' in str(form.errors):
                    return JsonResponse({'status': 'error', 'message': 'This password is too common.'})
                elif 'A user with that username already exists.' in str(form.errors):
                    return JsonResponse({'status': 'error', 'message': 'A user with that username already exists.'})
                elif 'The two password fields didn’t match.' in str(form.errors):
                    return JsonResponse({'status': 'error', 'message': 'The two password fields didn’t match.'})
                elif 'This field is required.' in str(form.errors):
                    return JsonResponse({'status': 'error', 'message': 'This field is required.'})
                else:
                    return JsonResponse({'status': 'error', 'message': 'Unknow error'})

        except Exception as e:
            # Обработка ошибок
            print('Error during registration:', str(e))
            response_data = {'status': 'error', 'message': 'An error occurred during registration'}
            return JsonResponse(response_data, status=500)

    # Обработка неверного метода запроса
    else:
        response_data = {'status': 'error', 'message': 'Invalid request method'}
        return JsonResponse(response_data, status=400)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            # Используем нашу форму для обработки данных
            form = EmailAuthenticationForm(request, json.loads(request.body.decode('utf-8')))

            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user_profile = UserProfile.objects.filter(user__username=username).first()

                if user_profile and user_profile.is_blocked:
                    return JsonResponse({'status': 'error', 'message': 'User is banned'})

                user = authenticate(request, username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    if request.user.is_authenticated:
                        user_profile.is_online = True
                        user_profile.save()
                        django_session = Session.objects.get(session_key=request.session.session_key)

                        # Пример успешного ответа с куками сессии
                        response_data = {
                            'status': 'success',
                            'message': 'Login successful',
                            'sessionid': django_session.session_key,
                            'session_expire_at': django_session.expire_date.timestamp(),
                        }
                        response = JsonResponse(response_data)

                        # Устанавливаем куки сессии в ответе
                        response.set_cookie('sessionid', django_session.session_key, expires=django_session.expire_date,
                                            secure=False, httponly=False)

                        return response

                    else:
                        return JsonResponse({'status': 'error', 'message': 'User is alredy logined'})
            else:
                print(form.errors)

                if 'This field is required.' in str(form.errors):
                    return JsonResponse({'status': 'error', 'message': 'This field is required.'})
                elif "Please enter a correct username and password. Note that both fields may be case-sensitive." in \
                        str(form.errors):
                    return JsonResponse({'status': 'error', 'message': 'Please enter a correct username and password'})
                else:
                    return JsonResponse({'status': 'error', 'message': 'Unknow error'})

        except Exception as e:
            # Обработка ошибок
            print('Error during login:', str(e))
            response_data = {'status': 'error', 'message': 'i dont now what happened blyat'}
            return JsonResponse(response_data, status=500)

    # Обработка неверного метода запроса
    else:
        print(request.method)
        response_data = {'status': 'error', 'message': 'Invalid request method'}
        return JsonResponse(response_data, status=400)


@csrf_exempt
def logout_user(request):
    if request.method == 'POST':
        try:
            # Получаем данные из тела запроса
            data = json.loads(request.body.decode('utf-8'))

            # Извлекаем sessionid из данных запроса
            session_id_from_request = data.get('sessionid')

            # Выводим sessionid в консоль (можно использовать print для вывода в консоль)
            print(f'Session ID from request: {session_id_from_request}')

            # Завершаем сеанс пользователя с использованием переданного sessionid
            Session.objects.filter(session_key=session_id_from_request).delete()

            # Возвращаем успешный ответ
            response_data = {'status': 'success', 'message': 'User logged out successfully'}
            return JsonResponse(response_data)
        except Exception as e:
            # Обработка ошибок
            print('Error during logout:', str(e))
            response_data = {'status': 'error', 'message': 'An error occurred during logout'}
            return JsonResponse(response_data, status=500)
    else:
        # Обработка неверного метода запроса
        response_data = {'status': 'error', 'message': 'Invalid request method'}
        return JsonResponse(response_data, status=400)


@csrf_exempt
def get_user_data(request):
    if request.method == 'POST':
        try:
            # Получаем данные из тела запроса
            data = json.loads(request.body.decode('utf-8'))

            # Извлекаем sessionid из данных запроса
            session_id_from_request = data.get('sessionid')

            # Получаем объект сессии по переданному sessionid
            session = Session.objects.get(session_key=session_id_from_request)

            # Получаем пользователя из сессии
            user_id = session.get_decoded().get('_auth_user_id')
            user = User.objects.get(pk=user_id)

            return JsonResponse({'status': 'success', 'name': user.first_name, 'surname': user.last_name,
                                 'login': user.username,
                                 'email': user.email})

        except Session.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Session does not exist'}, status=300)
        except Exception as e:
            # Обработка других ошибок
            print('Error during user data retrieval:', str(e))
            return JsonResponse({'status': 'error', 'message': 'An error occurred during user data retrieval'},
                                status=500)
    else:
        # Обработка неверного метода запроса
        response_data = {'status': 'error', 'message': 'Invalid request method'}
        return JsonResponse(response_data, status=400)


@csrf_exempt
def create_user_category(request):
    if request.method == 'POST':
        try:
            # Получаем данные из тела запроса
            data = json.loads(request.body.decode('utf-8'))
            session_id_from_request = data.get('sessionid')

            # Получаем объект сессии по переданному sessionid
            session = Session.objects.get(session_key=session_id_from_request)

            # Получаем пользователя из сессии
            user_id = session.get_decoded().get('_auth_user_id')
            user = User.objects.get(pk=user_id)
            # Извлекаем значения из данных
            user_category_name = data.get('category_name')

            # Проверяем, существует ли категория с таким именем для данного пользователя
            existing_category = UserCategory.objects.filter(user=user, user_category_name=user_category_name).first()

            if existing_category is None:
                # Если категории не существует, создаем новую
                new_category = UserCategory(user=user, user_category_name=user_category_name)
                new_category.save()

                # Пример успешного ответа
                response_data = {'status': 'success', 'message': 'Category created successfully'}
                return JsonResponse(response_data)
            else:
                # Пример ответа, если категория уже существует
                response_data = {'status': 'error', 'message': 'Category already exists'}
                return JsonResponse(response_data, status=400)
        except Exception as e:
            # Обработка ошибок
            print('Error during category creation:', str(e))
            response_data = {'status': 'error', 'message': 'An error occurred during category creation'}
            return JsonResponse(response_data, status=500)

    # Обработка неверного метода запроса
    response_data = {'status': 'error', 'message': 'Invalid request method'}
    return JsonResponse(response_data, status=400)


@csrf_exempt
def add_news_to_category(request):
    if request.method == 'POST':
        try:
            # Получаем данные из тела запроса
            data = json.loads(request.body.decode('utf-8'))
            session_id_from_request = data.get('sessionid')

            # Получаем объект сессии по переданному sessionid
            session = Session.objects.get(session_key=session_id_from_request)

            # Получаем пользователя из сессии
            user_id = session.get_decoded().get('_auth_user_id')
            user = User.objects.get(pk=user_id)
            # Извлекаем значения из данных
            category_name = data.get('category_name')
            news_title = data.get('news_title')

            # Находим категорию пользователя
            user_category = UserCategory.objects.filter(user=user, user_category_name=category_name).first()

            if user_category is not None:
                # Находим новость по заголовку
                news = News.objects.filter(title=news_title).first()

                if news is not None:
                    # Добавление новости к выбранной категории
                    user_category.news.add(news)

                    # Пример успешного ответа
                    response_data = {'status': 'success', 'message': 'News added to category successfully'}
                    return JsonResponse(response_data)
                else:
                    # Пример ответа, если новость не найдена
                    response_data = {'status': 'error', 'message': 'News not found'}
                    return JsonResponse(response_data, status=404)
            else:
                # Пример ответа, если категория не найдена
                response_data = {'status': 'error', 'message': 'Category not found'}
                return JsonResponse(response_data, status=404)
        except Exception as e:
            # Обработка ошибок
            print('Error adding news to category:', str(e))
            response_data = {'status': 'error', 'message': 'An error occurred while adding news to category'}
            return JsonResponse(response_data, status=500)

    # Обработка неверного метода запроса
    response_data = {'status': 'error', 'message': 'Invalid request method'}
    return JsonResponse(response_data, status=400)


@csrf_exempt
def get_user_categories(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            # Извлекаем sessionid из данных запроса
            session_id_from_request = data.get('sessionid')

            # Получаем объект сессии по переданному sessionid
            session = Session.objects.get(session_key=session_id_from_request)

            # Получаем пользователя из сессии
            user_id = session.get_decoded().get('_auth_user_id')
            user = User.objects.get(pk=user_id)
            # Получаем все категории пользователя
            user_categories = UserCategory.objects.filter(user=user)

            # Преобразуем категории в список словарей
            categories_list = [{'name': category.user_category_name} for category in user_categories]
            response_data = {
                'status': True,
                'name': [category['name'] for category in categories_list]
            }
            # Возвращаем список категорий в формате JSON

            return JsonResponse(response_data)
        except Exception as e:
            # Обработка ошибок
            print('Error getting user categories:', str(e))
            response_data = {'status': 'error', 'message': 'An error occurred while getting user categories'}
            return JsonResponse(response_data, status=500)

    # Обработка неверного метода запроса
    response_data = {'status': 'error', 'message': 'Invalid request method'}
    return JsonResponse(response_data, status=400)


@csrf_exempt
def del_user_categories(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            # Извлекаем sessionid из данных запроса
            session_id_from_request = data.get('sessionid')
            user_category_name = data.get('categoryName')
            # Получаем объект сессии по переданному sessionid
            session = Session.objects.get(session_key=session_id_from_request)

            # Получаем пользователя из сессии
            user_id = session.get_decoded().get('_auth_user_id')
            user = User.objects.get(pk=user_id)

            user_category = UserCategory.objects.get(user=user, user_category_name=user_category_name)

            # Удаляем объект UserCategory без удаления связанных новостей
            user_category.delete()

            response_data = {'status': 'success'}
            return JsonResponse(response_data)
        except Exception as e:
            # Обработка ошибок
            print('Error getting user categories:', str(e))
            response_data = {'status': 'error', 'message': 'An error occurred while getting user categories'}
            return JsonResponse(response_data, status=500)

    # Обработка неверного метода запроса
    response_data = {'status': 'error', 'message': 'Invalid request method'}
    return JsonResponse(response_data, status=400)


@csrf_exempt
def del_news_from_user_category(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            # Извлекаем sessionid из данных запроса
            session_id_from_request = data.get('sessionid')
            user_category_name = data.get('categoryName')
            news_title = data.get('title')

            # Получаем объект сессии по переданному sessionid
            session = Session.objects.get(session_key=session_id_from_request)

            # Получаем пользователя из сессии
            user_id = session.get_decoded().get('_auth_user_id')
            user = User.objects.get(pk=user_id)

            # Получаем категорию пользователя
            user_category = UserCategory.objects.get(user=user, user_category_name=user_category_name)

            # Получаем объект новости из общей базы данных
            news = News.objects.get(title=news_title)

            # Удаляем связь между категорией пользователя и новостью
            user_category.news.remove(news)

            return JsonResponse({'status': 'success', 'message': 'News removed from user category'})
        except Exception as e:
            # Обработка ошибок
            print('Error during deleting news from user category:', str(e))
            response_data = {'status': 'error', 'message': 'An error occurred during the process'}
            return JsonResponse(response_data, status=500)

    # Обработка неверного метода запроса
    response_data = {'status': 'error', 'message': 'Invalid request method'}
    return JsonResponse(response_data, status=400)


@csrf_exempt
def get_news_from_user_categories(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            # Извлекаем sessionid из данных запроса
            session_id_from_request = data.get('sessionid')
            user_category_name = data.get('userCategoryName')

            # Получаем объект сессии по переданному sessionid
            session = Session.objects.get(session_key=session_id_from_request)

            # Получаем пользователя из сессии
            user_id = session.get_decoded().get('_auth_user_id')
            user = User.objects.get(pk=user_id)

            # Получаем категорию пользователя
            user_category = UserCategory.objects.get(user=user, user_category_name=user_category_name)

            # Получаем все новости в данной категории
            news_list = user_category.news.all()
            response_data = {
                'success': True,
                'news': []
            }
            # Формируем список новостей

            for news in news_list:
                assets = news.asset_set.all()
                asset_info = {
                    'images': assets[0].images if assets else None,
                    'videos': assets[0].videos if assets else None,
                }

                news_item = {
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
                }
                response_data['news'].append(news_item)
            return JsonResponse(response_data)
        except Exception as e:
            # Обработка ошибок
            print('Error during getting news from user category:', str(e))
            response_data = {'status': 'error', 'message': 'An error occurred during the process'}
            return JsonResponse(response_data, status=500)

    # Обработка неверного метода запроса
    response_data = {'status': 'error', 'message': 'Invalid request method'}
    return JsonResponse(response_data, status=400)


