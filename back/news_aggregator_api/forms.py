from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserCategory, News


class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))


class UserCategoryForm(forms.ModelForm):
    class Meta:
        model = UserCategory
        fields = ['user_category_name', 'news']


class AddNewsToCategoryForm(forms.Form):
    user_category = forms.ModelChoiceField(queryset=UserCategory.objects.all(), label='User Category')
    news = forms.ModelChoiceField(queryset=News.objects.all(), label='News')