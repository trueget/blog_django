from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticlesForm, CommentsForm
from .models import Articles, Comments
from django.contrib.auth.models import User
from user_page.models import UserProfile
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q


'''главная'''
def index(request):
    '''все статьи разбитые построчно'''
    all_articles = Articles.objects.order_by('-create_date')
    for article in all_articles:
        article.text_article = article.text_article.replace('\r', '').split('\n')

    '''пагинация'''
    paginator = Paginator(all_articles, 10)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    '''форма создания статьи и запись в бд'''
    try:
        user = User.objects.get(username=request.user.username)
    except:
        user = None

    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            made_article = Articles.objects.create(username=user)
            made_article.name_article = form.cleaned_data['name_article']
            if form.cleaned_data['img_article']:
                made_article.img_article = form.cleaned_data['img_article']
            made_article.text_article = form.cleaned_data['text_article']
            made_article.article_section = form.cleaned_data['article_section']
            made_article.save()
            return redirect('/')
        else:
            error = 'Форма не валидна'
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    if user:
        data_user, created = UserProfile.objects.get_or_create(user=user)
    else:
        data_user = None

    '''4 статьи пользователя'''
    articles = Articles.objects.filter(username=user).order_by('-create_date')[:4]

    amount_all_articles = len(Articles.objects.all())

    return render(request, 'blog/index.html', {
        'userr': user, 
        'page_object': page_object, 
        'data': data, 
        'articles': articles,
        'data_user': data_user,
        'amount_all_articles': amount_all_articles
        })


'''все авторы с количеством статтей у каждого'''
def all_authors(request):
    all_articles = Articles.objects.all()
    user = User.objects.get(username=request.user.username)
    data_user =  UserProfile.objects.get(user=user)

    '''все статьи которые хранятся в бд'''
    all_articles_authors = [i.username for i in all_articles]

    '''все авторы с количеством статтей у каждого по отдельности'''
    authors = [(j, j.id, all_articles_authors.count(j)) for j in set(all_articles_authors)]

    return render(request, 'blog/authors.html', {'data_authors':authors, 'userr': user, 'data_user': data_user})


'''статья на моей странице с комментами'''
class BlogDetail(DetailView):
    model = Articles
    template_name = 'blog/one_article.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_object = Articles.objects.get(name_article=context['article'])
        article_object.views += 1
        article_object.save()
        comments = Comments.objects.filter(which_article=article_object)
        context['text_article'] = article_object.text_article.replace('\r', '').split('\n')
        context['comment_form'] = CommentsForm()
        context['comments'] = comments

        try:
            user = User.objects.get(username=self.request.user.username)
        except:
            user = None
        if user:
            data_user, created = UserProfile.objects.get_or_create(user=user)
        else:
            data_user = None
        context['data_user'] = data_user
        context['userr'] = user
        context['link_for_share'] = 'http://127.0.0.1:8000' + self.request.path
        
        return context

    def post(self , request , *args , **kwargs):
        if self.request.method == 'POST':
            comment_form = CommentsForm(self.request.POST)
            if comment_form.is_valid():
                user = User.objects.get(username=self.request.user)
                profile = UserProfile.objects.get(user_id=user.id)
                content = comment_form.cleaned_data['content']
                try:
                    parent = comment_form.cleaned_data['parent']
                except:
                    parent = None
            new_comment = Comments(content=content , author=self.request.user , which_article=self.get_object() , parent=parent, link_img=profile)
            new_comment.save()
            return redirect(self.request.path_info)



'''статья с комментами на странице пользователя'''
def article_on_user_page(request, **kwargs):
    article = Articles.objects.get(id=kwargs['article_id'])
    article.views += 1
    article.save()
    article.text_article = article.text_article.replace('\r', '').split('\n')
    user = User.objects.get(id=kwargs['user_id'])
    user_profile = UserProfile.objects.get(user=user)
    comments = Comments.objects.filter(which_article=article)
    link_for_share = 'http://127.0.0.1:8000' + request.path

    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            try:
                parent = form.cleaned_data['parent']
            except:
                parent = None
            img_user_profile = UserProfile.objects.get(user_id=request.user.id)
            new_comment = Comments(content=content , author=request.user , which_article=article , parent=parent, link_img=img_user_profile)
            new_comment.save()

            return render(request, 'blog/user_one_article.html', {
                'userr': user,
                'user_profile': user_profile,
                'article': article,
                'comments': comments
            })
        else:
            error = ' Форма не валидна'
            return render(request, 'blog/user_one_article.html', {'form': form})

    else:
        form = CommentsForm()
        return render(request, 'blog/user_one_article.html', {
            'userr': user,
            'user_profile': user_profile,
            'article': article,
            'comments': comments,
            'form': form,
            'link_for_share': link_for_share

        })


'''разделы статтей'''
class ArticlesSection(ListView):

    model = Articles
    template_name = 'blog/article_section.html'

    def get_context_data(self , **kwargs):
        context = super(ArticlesSection, self).get_context_data(**kwargs)
        section_article = {
            'finance': 'финансы',
            'space': 'космос',
            'IT': 'IT',
            'art': 'искусство',
            'nature': 'природа',
            'design': 'дизайн',
            'games': 'игр',
            'other': 'другое'
        }
        try:
            articles_object = Articles.objects.filter(article_section=section_article[self.kwargs['article_section']]).order_by('-create_date')
            for article in articles_object:
                article.text_article = article.text_article.replace('\r', '').split('\n')
        except:
            articles_object = None

        try:
            user = User.objects.get(username=self.request.user.username)
        except:
            user = None

        if user:
            data_user, created = UserProfile.objects.get_or_create(user=user)
        else:
            data_user = None

        context['userr'] = user
        context['data_user'] = data_user
        context['articles_section'] = articles_object

        return context


@login_required
def like_article(request, pk):
    article = get_object_or_404(Articles, id=pk)
    user = request.user

    if user in article.likes.all():
        article.likes.remove(user)
        return redirect('/')
    else:

        article.likes.add(user) 
        article.save()
        return redirect('/')



'''поиск'''
class SearchResultsView(ListView):
    model = Articles
    template_name = 'blog/search_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            user = User.objects.get(username=self.request.user.username)
        except:
            user = None
        if user:
            data_user, created = UserProfile.objects.get_or_create(user=user)
        else:
            data_user = None
        search_text = self.request.GET.get('search_text')
        search_articles = Articles.objects.filter(Q(name_article__icontains=search_text) | Q(text_article__icontains=search_text))
        for article in search_articles:
            article.text_article = article.text_article.replace('\r', '').split('\n')

        context['userr'] = user
        context['data_user'] = data_user
        context['search_articles'] = search_articles

        return context


'''удаление статтей из бд'''
def delete(request, id):
    try:
        article = Articles.objects.get(id=id)
        article.delete()
        return redirect('my_articles')
    except Articles.DoesNotExist:
        return HttpResponseNoteFound('<h2>Клиент не найден</h2>')


'''мои публикации'''
def my_articles(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    articles = Articles.objects.filter(username=user).order_by('-create_date')
    for article in articles:
        article.text_article = article.text_article.replace('\r', '').split('\n')

    '''пагинация'''
    paginator = Paginator(articles, 10)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return render(request, 'blog/my_articles.html', {
        'data_user': user_profile, 
        'userr': user, 
        'articles': articles,
        'page_object': page_object
        })
