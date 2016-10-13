from django.shortcuts import render
from django.utils import timezone
from .models import Post

def fullsite(request):
    posts = Post.objects.order_by('date')
    return render(request, 'core/post_list.html', {'posts': posts})