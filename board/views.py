from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from datetime import date
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-created_at')  # 최신순 정렬
    return render(request, 'board/index.html', {'posts': posts})