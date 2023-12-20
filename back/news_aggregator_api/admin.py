from django.contrib import admin
from .models import System, UserCategory, Category, Country, Region, City, Source, News, Asset, Celebrity, FamousEvent, FamousDate

# Register your models here.

admin.site.register(System)
admin.site.register(UserCategory)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(Source)
admin.site.register(News)
admin.site.register(Asset)
admin.site.register(Celebrity)
admin.site.register(FamousEvent)
admin.site.register(FamousDate)