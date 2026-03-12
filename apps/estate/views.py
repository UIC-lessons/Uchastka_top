from django.shortcuts import render

from apps.estate.models import Estate


def home(request):
    estates = Estate.objects.all()
    image = estates[0].images.first()
    return render(request, "index.html", context={"estates": estates, "image": image})

def about(request):
    return render(request, "about.html",)

def property(request):
    return render(request, "property-grid.html",)

def blog(request):
    return render(request, "blog-grid.html",)