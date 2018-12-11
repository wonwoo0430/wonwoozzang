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

def A(request): return render(request, 'blog/A.html', {})
def AA(request): return render(request, 'blog/AA.html', {})
def AABA(request): return render(request, 'blog/AABA.html', {})
def AAC(request): return render(request, 'blog/AAC.html', {})
def AAL(request): return render(request, 'blog/AAL.html', {})
def AAN(request): return render(request, 'blog/AAN.html', {})
def AAOI(request): return render(request, 'blog/AAOI.html', {})
def AAON(request): return render(request, 'blog/AAON.html', {})
def AAP(request): return render(request, 'blog/AAP.html', {})
def AAPL(request): return render(request, 'blog/AAPL.html', {})
def AAWW(request): return render(request, 'blog/AAWW.html', {})
def AAXN(request): return render(request, 'blog/AAXN.html', {})
