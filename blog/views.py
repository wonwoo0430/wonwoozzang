from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.http import HttpResponse
from django.template import loader


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def index(request):
    template = loader.get_template('blog/index.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))

def aapl(request):
    return render(request, 'blog/aapl.html', {})

def a(request):
    return render(request, 'blog/a.html', {})

def aaba(request):
    return render(request, 'blog/Altaba Inc(AABA).html', {})

def aa(request):
    return render(request, 'blog/Alcoa Corp(AA).html', {})

def aal(request):
    return render(request, 'blog/American Airlines Group Inc(AAL).html', {})
