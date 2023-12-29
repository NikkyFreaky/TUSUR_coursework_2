from django.contrib import admin
from .models import System, UserCategory, Category, Country, Region, City, Source, News, Asset, Celebrity, FamousEvent, \
    FamousDate, UserProfile

# Register your models here.

admin.site.register(System)
admin.site.register(UserCategory)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(Asset)
admin.site.register(Celebrity)
admin.site.register(FamousEvent)
admin.site.register(FamousDate)
admin.site.register(UserProfile)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_filter = ('categories', 'countries', 'event_date',)


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_filter = ('source_name',)