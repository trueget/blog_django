from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PublishState

# Create your views here.

def index_page(request):
    return render(request, 'blog/index.html')


# def publish_page(request):
#     if request.method == 'POST':
#         form = PublishState(request.POST)
#         if form.is_valid():
#     return render(request, 'blog/publish.html')

def publish_page(request):
    publish_stat = PublishState()
    return render(request, 'blog/publish.html', {'publish_stat': publish_stat})



def news_page(request):
    return render(request, 'blog/index.html')


# def about_page(request):
#     return render(request, 'about.html')
