from django.urls import path

from apps.estate.views import home, about, property, blog, contact, property_single, blog_single, agents_grid, agent_single


urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("property/", property, name="property-grid"),
    path("blog/", blog, name="blog-grid"),
    path("contact/", contact, name="contact"),
    path("property-single/", property_single, name="property_single"),
    path("blog-single/", blog_single, name="blog_single"),
    path("agents/", agents_grid, name="agents_grid"),
    path("agent/", agent_single, name="agent_single"),
]