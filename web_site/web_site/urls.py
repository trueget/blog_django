from django.contrib import admin
from django.urls import path
from blog import views as blog_views
from users import views as user_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.index_page),
    path('create_article/', blog_views.create_article),
    path('news/', blog_views.news_page, name='news'),
    path('articles/', blog_views.articles),
    path(r'articles/delete/<int:id>', blog_views.delete),
    path('register/', user_views.register_user, name='register'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''path('admin/', views.admin.site.urls),'''
