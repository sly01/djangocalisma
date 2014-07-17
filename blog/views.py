from django.shortcuts import render_to_response
from models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render_to_response('posts.html', locals())