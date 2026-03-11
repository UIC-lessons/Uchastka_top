from django.contrib import admin
from apps.common.models import Currency, State, Region, Service, Media

# Register your models here.

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]
    search_fields = [
        "name"
    ]
    fields = [
        "name"
    ]


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = [
        "name", "state"
    ]
    search_fields = [
        "name", "state"
    ]
    fields = [
        "name", "state"
    ]

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]
    search_fields = [
        "name"
    ]
    fields = [
        "name"
    ]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        "name", "icon"
    ]
    search_fields = [
        "name"
    ]
    fields = [
        "name", "icon"
    ]


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = [
        "name", "created_at", "upload_at"
    ]
    search_fields = [
        "name"
        ]
    fields = [
        "name"
        ]