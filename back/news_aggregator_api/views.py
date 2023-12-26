from django.shortcuts import render, redirect
from .components.parser import parse_news
from .components.get_news import get_news
from .components.search_news import news_search
from .models import UserProfile, Group, System
from django.http import JsonResponse
import datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ExtendedUserCreationForm, EmailAuthenticationForm, UserCategoryForm, AddNewsToCategoryForm
from django.contrib.auth import authenticate, login as auth_login
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
def news_search_by_keywords(request):
    return news_search(request)

#  ниже простарнство для создания новых функций


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

                # Пример успешного ответа
                response_data = {'status': 'success', 'message': 'Registration successful'}
                return JsonResponse(response_data)
            else:
                # Пример ответа с ошибками формы
                response_data = {'status': 'error', 'errors': form.errors}
                return JsonResponse(response_data, status=400)
        except Exception as e:
            # Обработка ошибок
            print('Error during registration:', str(e))
            response_data = {'status': 'error', 'message': 'An error occurred during registration'}
            return JsonResponse(response_data, status=500)

    # Обработка неверного метода запроса
    response_data = {'status': 'error', 'message': 'Invalid request method'}
    return JsonResponse(response_data, status=400)


def login(request):
    if request.method == 'POST':
        try:
            # Получаем данные из тела запроса
            data = json.loads(request.body.decode('utf-8'))

            # Извлекаем значения username и password
            username = data.get('username')
            password = data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return JsonResponse({'status': 'success', 'message': 'Login successful'})


        except Exception as e:

            # Обработка ошибок

            print('Error during login:', str(e))

            response_data = {'status': 'error', 'message': 'Invalid username or password'}

            return JsonResponse(response_data, status=500)

            # Обработка неверного метода запроса

    response_data = {'status': 'error', 'message': 'Invalid request method'}
    return JsonResponse(response_data, status=400)


def logout(request):
    logout(request)
    return redirect('')


def create_user_category(request):  # РАБОТАЕТ ЧЕРЕЗ ТРИ ПИЗДЫ
    if request.method == 'POST':
        form = UserCategoryForm(request.POST)
        if form.is_valid():
            user_category = form.save(commit=False)
            user_category.user = request.user
            user_category.save()
            return redirect('../')  # замените 'user_category_list' на URL вашего списка категорий
    else:
        form = UserCategoryForm()
    return render(request, 'create_user_category.html', {'form': form})


def add_news_to_category(request):  # РАБОТАЕТ ЧЕРЕЗ ТРИ ПИЗДЫ
    if request.method == 'POST':
        form = AddNewsToCategoryForm(request.POST)
        if form.is_valid():
            user_category = form.cleaned_data['user_category']
            news = form.cleaned_data['news']

            # Добавление новости к выбранной категории
            user_category.news.add(news)

            return redirect('../')  # замените 'user_category_list' на URL вашего списка категорий

    else:
        form = AddNewsToCategoryForm()

    return render(request, 'add_news_to_category.html', {'form': form})