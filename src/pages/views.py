from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    my_context = {
        'title': 'Home'
    }
    return render(request, "home.html", my_context)


def contact_view(request, *args, **kwargs):
    my_context = {
        'title': 'Contact'
    }
    return HttpResponse("<h1>Contact Page</h1>", my_context)
