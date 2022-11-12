from django.contrib import admin
from django.urls import path
from blog import views as blog_views
from users import views as user_views
from user_page import views as user_page_views
from news import views as news_views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', blog_views.index, name='index'),
    path('about_blog/', blog_views.about_blog, name='about_blog'),
    path('help_page/', blog_views.help_page, name='help_page'),

    path('create_article/', blog_views.create_article, name='create_article'),

    path('articles/', blog_views.articles, name='articles'),
    path('my_articles/', blog_views.my_articles, name='my_articles'),
    # path(r'article/id/<int:id>', blog_views.one_article, name='one_article'),
    # path(r'article/id/<int:id>', blog_views.BlogDetail.as_view(), name='one_article'),
    path(r'article/id/<slug:pk>', blog_views.BlogDetail.as_view(), name='one_article'),

    path(r'articles/delete/<int:id>', blog_views.delete),

    path('authors/', blog_views.all_authors, name='authors'),

    path('register/', user_views.register_user, name='register'),
    path('login/', user_views.Login, name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='blog/index.html'), name='logout'),
    path('activation/', user_views.activation_user, name='activation'),

    path('my_page/', user_page_views.update_profile, name='my_page'),
    path(r'user/id/<int:user_id>/', user_page_views.user_page, name='user_page'),

    path('news/', news_views.news, name='news'),
    path('page_finance/', news_views.page_finance, name='page_finance'),
    path('page_europe/', news_views.page_europa, name='page_europe'),
    path('page_dayli/', news_views.page_dayli, name='page_dayli'),
    path('page_nature/', news_views.page_nature, name='page_nature'),
    path('page_power/', news_views.page_power, name='page_power'),
    path('page_sport/', news_views.page_sport, name='page_sport'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
