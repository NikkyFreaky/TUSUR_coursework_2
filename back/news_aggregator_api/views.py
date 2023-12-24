from django.shortcuts import render, redirect
from .components.parser.parser import parse_news
from .components.crud.get_news import get_news
from .models import News, Country, UserProfile, User, Group, System
from django.contrib.auth.models import Permission
from django.http import JsonResponse
import datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ExtendedUserCreationForm, EmailAuthenticationForm, UserCategoryForm, AddNewsToCategoryForm
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.

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


def get_news_for_country(request):  # сам эндпоинт

    if request.method == 'GET':
        country_name = request.GET.get('country_name')
        try:
            parse_news(country_name)
            country = Country.objects.get(country_name=country_name)
            news_by_country = News.objects.filter(countries=country)
            news_data = [
                {
                    'title': news.title,
                    'description': news.description,
                    'event_date': news.event_date,
                    'publication_date': news.publication_date,
                    # добавить ругие поля которые надо выдать на фронт
                }
                for news in news_by_country
            ]
            return JsonResponse({'news': news_data})
        except Country.DoesNotExist:
            return JsonResponse({'error': 'Страна не найдена'}, status=404)
    return redirect("../")


def scrape(request):
    if request.method == 'GET':
        country_name = request.GET.get('country_name')

        parse_news(country_name)
    return redirect("../")


def default(request):
    return render(request, 'default.html')

#  ниже простарнство для создания новых функций


def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            print('register true')
            # Создаем пользователя
            user = form.save()


            user_group, created = Group.objects.get_or_create(name='Пользователь')
            user.groups.add(user_group)


            # Копируем права из группы в пользователя
            for permission in user_group.permissions.all():
                user.user_permissions.add(permission)

            system, created = System.objects.get_or_create(name='alfa test', version='0.0.1')

            # Создаем профиль пользователя
            UserProfile.objects.create(user=user, system=system)

            auth_login(request, user)
            return redirect('../')
        else:
            print('Form errors:', form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('../')
        else:
            print('Form errors:', form.errors)
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


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