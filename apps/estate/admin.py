from django.contrib import admin
from apps.estate.models import Estate_Agent, Estate, EstateAgentComment, EstateCategory, Amenities
# Register your models here.

@admin.register(Estate_Agent)
class EstateAgentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "last_name",
        "phone",
        "email",
    ]
    search_fields = [
        "name",
        "last_name",
        "email",
        "phone",
    ]
    fields = [
        "name",
        "last_name",
        "bio",
        "avatar",
        "phone",
        "mobile",
        "email",
        "telegram",
        "whatsapp",
        "instagram",
        "facebook",
        "x",
    ]


@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    list_display = [
        "name", "agent", "category","state","region","area", "price", "currency", "longitude", "latitude", "description", "garage",
    ]
    filter_horizontal = ("images", "amenities")
    search_fields = [
        "name", "category", "state", "region"
    ]

    fields = [
        "name", "agent", "category" , "state" , "region" , "address" , "status" , "area" , "beds" , "bath" , "price", "currency", "longitude", "latitude", "description", "amenities", "garage"
    ]


@admin.register(EstateCategory)
class EstataCategoryAdmin(admin.ModelAdmin):
    list_display = [ "name" ]
    search_fields = ["name"]
    fields = ["name"]

@admin.register(EstateAgentComment)
class EstateAgentCommentAdmin(admin.ModelAdmin):
    list_display = ["name", "comment"]
    search_fields = ["name", "email"]
    fields = ["name", "email", "comment"]


@admin.register(Amenities)
class AmenitiesAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    fields = ["name"]
