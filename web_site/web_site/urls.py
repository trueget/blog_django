from django.contrib import admin
from django.urls import path
from blog import views as blog_views
from users import views as user_views
from user_page import views as user_page_views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth


urlpatterns = [
    path('admin/', admin.site.urls),


    path('', blog_views.index_page, name='index'),
    path('create_article/', blog_views.create_article, name='create_article'),
    path('news/', blog_views.news_page, name='news'),
    path('articles/', blog_views.articles, name='articles'),
    path(r'articles/delete/<int:id>', blog_views.delete),
    path('register/', user_views.register_user, name='register'),
    path('login/', user_views.Login, name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='blog/index.html'), name='logout'),
    path('activation/', user_views.activation_user, name='activation'),
    path('user_page/', user_page_views.update_profile, name='user_page'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
