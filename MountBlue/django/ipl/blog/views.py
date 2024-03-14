from django.shortcuts import render
from .models import Post

# from django.http import HttpResponse
# return HttpResponse("<h1>Blog Home</h1>")


def home(request):
    return render(request, "blog/home.html", {"posts": Post.objects.all()})


def about(request):
    return render(request, "blog/about.html", {"posts": Post.objects.all()})
