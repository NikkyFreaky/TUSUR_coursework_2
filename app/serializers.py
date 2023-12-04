from rest_framework import serializers
from .models import System, User, UserCategory, News, Source, Asset, Category, Celebrity, FamousEvent, FamousDate, Country, Region, City

class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCategory
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CelebritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrity
        fields = '__all__'

class FamousEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamousEvent
        fields = '__all__'

class FamousDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamousDate
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'