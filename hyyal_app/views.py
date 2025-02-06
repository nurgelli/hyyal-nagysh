from django.shortcuts import render
from .models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, "./hyyal/post_list.html", {'posts': posts})
    


def post_detail(request, post_id):
    post = get_object(Post, id=post_id)
    return render(request, './hyyal/post_detail.html', {'post': post})
