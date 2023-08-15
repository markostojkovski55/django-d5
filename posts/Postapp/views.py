from django.shortcuts import render
from .models import Post
from .forms import PostForm


# Create your views here.

def index(request):
    return render(request, "index.html")


def post(request):
    queryset = Post.objects.filter(author=request.user).all()
    context = {"posts": queryset, "form": PostForm}
    return render(request, "post.html", context=context)


def add(request):
    queryset = Post.objects.filter(author=request.user).all()
    context = {"adds": queryset, "form": PostForm}
    return render(request, "add.html", context=context)


def profile(request):
    return render(request, "profile.html")


def blockedUsers(request):
    queryset = Post.objects.filter(author=request.user).all()
    context = {"blocks": queryset, "form": PostForm}
    return render(request, "blockedUsers.html", context=context)