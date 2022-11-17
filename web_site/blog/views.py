from django.shortcuts import render, redirect
from .forms import ArticlesForm, CommentsForm
from .models import Articles, Comments
from django.contrib.auth.models import User
from user_page.models import UserProfile
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator


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
            made_article.save()
            return redirect('/')
        else:
            error = 'Форма не валидна'
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    data_user, created = UserProfile.objects.get_or_create(user=user)

    '''4 статьи пользователя'''
    articles = Articles.objects.filter(username=user).order_by('-create_date')[:4]
        # return render(request, 'blog/index.html', {'all_articles': all_articles})

    return render(request, 'blog/index.html', {
        'user': user, 
        'page_object': page_object, 
        'data': data, 
        'articles': articles,
        'data_user': data_user
        })


'''удаление статтей из бд'''
def delete(request, id):
    try:
        article = Articles.objects.get(id=id)
        article.delete()
        return render(request, 'blog/articles.html')
    except Articles.DoesNotExist:
        return HttpResponseNoteFound('<h2>Клиент не найден</h2>')


'''публикации пользователя'''
def my_articles(request):
    user = User.objects.get(username=request.user.username)
    user_profile = UserProfile.objects.get(user=user)
    articles = Articles.objects.filter(username=user).order_by('-create_date')
    for article in articles:
        article.text_article = article.text_article.replace('\r', '').split('\n')
    return render(request, 'blog/my_articles.html', {'my_articles': articles, 'img': user_profile.user_avatar})


def all_authors(request):
    authors = Articles.objects.all()
    return render(request, 'blog/authors.html', {'authors': authors})


'''страница одной статьи с комментами'''
class BlogDetail(DetailView):
    model = Articles
    template_name = 'blog/one_article.html'
    context_object_name = 'article'

    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        article_object = Articles.objects.get(name_article=context['article'])
        comments = Comments.objects.filter(which_article=article_object)
        context['text_article'] = article_object.text_article.replace('\r', '').split('\n')
        context['comment_form'] = CommentsForm()
        context['comments'] = comments

        try:
            user = User.objects.get(username=self.request.user.username)
        except:
            user = None
        data_user, created = UserProfile.objects.get_or_create(user=user)
        context['data_user'] = data_user
        context['user'] = user
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




def article_on_user_page(request, **kwargs):
    article = Articles.objects.get(id=kwargs['article_id'])
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
                'user': user,
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
            'user': user,
            'user_profile': user_profile,
            'article': article,
            'comments': comments,
            'form': form,
            'link_for_share': link_for_share

        })





# class ArtivcleOnUserPage(DetailView):
#     template_name = 'blog/user_one_article.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         article_object = Articles.objects.get(name_article=context['article'])
#         comments = Comments.objects.filter(which_article=article_object)

#         return 







# def article_on_user_page(request, **kwargs):
#     article = Articles.objects.get(id=kwargs['article_id'])
#     user = User.objects.get(id=kwargs['user_id'])
#     user_profile = UserProfile.objects.get(user=user)
#     article.text_article = article.text_article.replace('\r', '').split('\n')
#     comments = Comments.objects.filter(which_article=article)
#     return render(request, 'blog/user_one_article.html', {
#         'user': user,
#         'user_profile': user_profile,
#         'article': article,
#         'comments': comments
#     })



'''страница статтей
плучение данных из бд и выгрузка на главную страницу'''
# def articles(request):
#     all_articles = Articles.objects.order_by('-create_date')
#     for article in all_articles:
#         article.text_article = article.text_article.replace('\r', '').split('\n')
#     return render(request, 'blog/articles.html', {'all_articles': all_articles})


# '''каждая статья отдельно'''
# def one_article(request, id):
#     article = Articles.objects.get(id=id)
#     article.text_article = article.text_article.replace('\r', '').split('\n')
#     return render(request, 'blog/one_article.html', {'article': article})


# def index(request):
#     return render(request, 'blog/index.html')

# '''главная о блоге'''
# def about_blog(request):
#     return render(request, 'blog/about_blog.html')


# '''страница помощи'''
# def help_page(request):
#     return render(request, 'blog/help_page.html')


# '''создание статьи и запись данных из формы в бд'''
# def create_article(request):
#     user = User.objects.get(username=request.user.username)
#     print(user)
#     error = ''
#     if request.method == 'POST':
#         form = ArticlesForm(request.POST, request.FILES)
#         if form.is_valid():
#             made_article = Articles.objects.create(username=user)
#             made_article.name_article = form.cleaned_data['name_article']
#             made_article.img_article = form.cleaned_data['img_article']
#             made_article.text_article = form.cleaned_data['text_article']
#             made_article.save()
#             return redirect('/')
#         else:
#             error = 'Форма была неверной!'

#     form = ArticlesForm()

#     data = {
#         'form': form,
#         'error': error
#     }
#     return render(request, 'blog/create_article.html', data)
