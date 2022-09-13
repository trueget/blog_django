from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import CreateArticle

import datetime

# Create your views here.

def index_page(request):
    return render(request, 'blog/index.html')


# def publish_page(request):
#     if request.method == 'POST':
#         form = PublishState(request.POST)
#         if form.is_valid():
#     return render(request, 'blog/publish.html')


'''
    if request.method == 'POST':
        nick_name = request.POST.get('nick_name')
        name_article = request.POST.get('name_article')
        img_article = request.POST.get('img_article')
        text_article = request.POST.get('text_article')
        output = {'nick_name': nick_name,
                    'name_article':name_article,
                    'img_article': img_article,
                    'text_article': text_article
                    }
        return HttpResponse()
'''


def create_article(request):
    if request.method == 'POST':
        nick_name = request.POST.get('nick_name')
        name_article = request.POST.get('name_article')
        img_article = request.POST.get('img_article')
        text_article = request.POST.get('text_article')
        date = datetime.datetime.now()
        output = {'nick_name': nick_name,
                    'name_article':name_article,
                    'img_article': img_article,
                    'text_article': text_article,
                    'date': date
                    }
        return render(request, 'blog/index.html', output)
        # return HttpResponse(request, 'blog/index.html', output)
    else:
        create_article = CreateArticle()
        return render(request, 'blog/create_article.html', {'create_article': create_article})



# def create_article(request):
#     create_article = CreateArticle()
#     return render(request, 'blog/create_article.html', {'create_article': create_article})



def news_page(request):
    return render(request, 'blog/index.html')


# def about_page(request):
#     return render(request, 'about.html')
