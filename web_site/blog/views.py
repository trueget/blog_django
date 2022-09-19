from django.shortcuts import render, redirect
from .forms import ArticlesForm
from .models import Articles


'''страница статтей
плучение данных из бд и выгрузка на главную страницу'''
def articles(request):
    all_articles = Articles.objects.order_by('-create_date')
    return render(request, 'blog/articles.html', {'all_articles': all_articles})


'''главная страница'''
def index_page(request):
    return render(request, 'blog/index.html')


'''страница новостей'''
def news_page(request):
    return render(request, 'blog/index.html')


'''запись данных из формы в бд'''
def create_article(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма была неверной!'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'blog/create_article.html', data)
