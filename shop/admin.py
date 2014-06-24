from django.contrib import admin
from shop.models import Website, Plan, Feature, Carousel


class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain', 'plan', 'created')


class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price')


class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 50
    search_fields = ['name', 'description']


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 50
    search_fields = ['name', 'description']


admin.site.register(Website, WebsiteAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Plan, PlanAdmin)

