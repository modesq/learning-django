from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    my_context = {
        "username": request.user,
        "user_email": request.user.email,
        "my_list": [2345, 23532, 5765],
    }
    return render(request, "home.html", my_context)


def about_view(request, *args, **kwargs):
    my_context = {
        "username": request.user,
        "user_email": request.user.email,
        "my_list": [2345, 23532, 5765],
    }
    print(request.user)
    return render(request, "about.html", my_context)
