from gc import get_objects
from django.shortcuts import render, redirect
from .forms import ArticlesForm, CommentsForm
from .models import Articles, Comments
from django.contrib.auth.models import User
from user_page.models import UserProfile
from django.views.generic.detail import DetailView


'''страница статтей
плучение данных из бд и выгрузка на главную страницу'''
def articles(request):
    all_articles = Articles.objects.order_by('-create_date')
    for article in all_articles:
        article.text_article = article.text_article.replace('\r', '').split('\n')
    return render(request, 'blog/articles.html', {'all_articles': all_articles})


# '''каждая статья отдельно'''
# def one_article(request, id):
#     article = Articles.objects.get(id=id)
#     article.text_article = article.text_article.replace('\r', '').split('\n')
#     return render(request, 'blog/one_article.html', {'article': article})


def index(request):
    return render(request, 'blog/index.html')

'''главная о блоге'''
def about_blog(request):
    return render(request, 'blog/about_blog.html')


'''страница помощи'''
def help_page(request):
    return render(request, 'blog/help_page.html')


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




class BlogDetail(DetailView):
    model = Articles
    template_name = 'blog/one_article.html'
    context_object_name = 'article'

    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        article_object = Articles.objects.get(name_article=context['article'])
        context['text_article'] = article_object.text_article.replace('\r', '').split('\n')
        context['comment_form'] = CommentsForm()
        return context





    #     data = super().get_context_data(**kwargs)
    #     print('='*100)
    #     # print(data)
    #     # print(self)
    #     # print('object', data['object'])
    #     print('article', data)
    #     # c = data['article']
    #     # print(c)

    #     # print('view', data['view'])
    #     print('='*100)
    #     data['comment_form'] = CommentsForm(instance=self.get_object())

        # connected_comments = Comments.objects.filter(which_article=self.get_object())
        # number_of_comments = connected_comments.count()
        # data['comments'] = connected_comments
        # data['no_of_comments'] = number_of_comments
        # data['comment_form'] = CommentsForm()
        # data['article'] =

        # return data

    # def post(self , request , *args , **kwargs):
    #     if self.request.method == 'POST':
    #         print('-------------------------------------------------------------------------------Reached here')
    #         comment_form = CommentsForm(self.request.POST)
    #         if comment_form.is_valid():
    #             content = comment_form.cleaned_data['content']
    #             try:
    #                 parent = comment_form.cleaned_data['parent']
    #             except:
    #                 parent=None
    #         new_comment = Comments(content=content , author=self.request.user , which_article=self.get_object() , parent=parent)
    #         new_comment.save()
    #         return redirect(self.request.path_info)
