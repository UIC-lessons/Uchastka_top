from django.shortcuts import render

from apps.estate.models import Estate


def home(request):
    estates = Estate.objects.prefetch_related("images").filter().order_by("-price")[:3]
    context = {"estates": estates, }
    return render(request, "index.html", context=context)


def about(request):
    return render(request, "about.html")


def property(request):
    return render(request, "property-grid.html")


def blog(request):
    return render(request, "blog-grid.html")


def contact(request):
    return render(request, "contact.html")


def property_single(request):
    return render(request, "property-single.html")



def blog_single(request):
    return render(request, "blog-single.html")



def agents_grid(request):
    return render(request, "agents-grid.html")



def agent_single(request):
    return render(request, "agent-single.html")