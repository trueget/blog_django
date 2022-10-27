from django.shortcuts import render, redirect
from .forms import ArticlesForm
from .models import Articles
from django.contrib.auth.models import User
from user_page.models import UserProfile


'''страница статтей
плучение данных из бд и выгрузка на главную страницу'''
def articles(request):
    all_articles = Articles.objects.order_by('-create_date')
    return render(request, 'blog/articles.html', {'all_articles': all_articles})


'''главная страница'''
def index_page(request):
    return render(request, 'blog/index.html')


'''запись данных из формы в бд'''
def create_article(request):
    user = User.objects.get(username=request.user.username)
    print(user)
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            made_article = Articles.objects.create(username=user)
            made_article.name_article = form.cleaned_data['name_article']
            made_article.img_article = form.cleaned_data['img_article']
            made_article.text_article = form.cleaned_data['text_article']
            made_article.save()
            return redirect('/')
        else:
            error = 'Форма была неверной!'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'blog/create_article.html', data)


'''удаление статтей из бд'''
def delete(request, id):
    try:
        article = Articles.objects.get(id=id)
        article.delete()
        return render(request, 'blog/index.html')
    except Articles.DoesNotExist:
        return HttpResponseNoteFound('<h2>Клиент не найден</h2>')


'''публикации пользователя'''
def my_articles(request):
    user = User.objects.get(username=request.user.username)
    user_profile = UserProfile.objects.get(user=user)
    articles = Articles.objects.filter(username=user)
    return render(request, 'blog/my_articles.html', {'my_articles': articles, 'img': user_profile.user_avatar})


def all_authors(request):
    authors = Articles.objects.all()
    return render(request, 'blog/authors.html', {'authors': authors})
