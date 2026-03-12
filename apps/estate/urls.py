from django.urls import path

from apps.estate.views import home, about, property, blog


urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("property/", property, name="property-grid"),
    path("blog/", blog, name="blog-grid"),

]