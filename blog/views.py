from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.
def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def home(request):
    return render(request, 'blog/home.html')

def board(request):
    return render(request, 'blog/board.html')

def cities(request):
    return render(request, 'blog/cities.html')

def orgs(request):
    return render(request, 'blog/orgs.html')
