from django.contrib import admin
from django.urls import path
from blog import views as blog_views
from users import views as user_views
from user_page import views as user_page_views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth
# from news import views as news_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.index, name='index'),
    path(r'articles/id=<int:pk>/', blog_views.BlogDetail.as_view(), name='one_article'),
    path(r'articles/like/id=<pk>/', blog_views.like_article, name='like_article'),
    path(r'section/<slug:article_section>/', blog_views.ArticlesSection.as_view(), name='articles_section'),
    path(r'search_article/', blog_views.SearchResultsView.as_view(), name='search_article'),
    path(r'users/id=<int:user_id>/articles/id=<int:article_id>/', blog_views.article_on_user_page , name='one_article_from_user'),
    path('authors/', blog_views.all_authors, name='authors'),
    path('register/', user_views.register_user, name='register'),
    path('login/', user_views.Login, name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='register/login.html', next_page='index'), name='logout'),
    path('activation/', user_views.activation_user, name='activation'),
    path('my_page/', user_page_views.update_profile, name='my_page'),
    path(r'users/id=<int:user_id>/', user_page_views.user_page, name='user_page'),
    path(r'articles/delete/<int:id>/', blog_views.delete),
    path('user/id=<user_id>/articles', blog_views.user_articles, name='user_articles'),

    # path('news/', news_views.news, name='news'),
    # path('page_finance/', news_views.page_finance, name='page_finance'),
    # path('page_europe/', news_views.page_europa, name='page_europe'),
    # path('page_dayli/', news_views.page_dayli, name='page_dayli'),
    # path('page_nature/', news_views.page_nature, name='page_nature'),
    # path('page_power/', news_views.page_power, name='page_power'),
    # path('page_sport/', news_views.page_sport, name='page_sport'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
