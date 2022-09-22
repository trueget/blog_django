from django.contrib import admin
from django.urls import path
from blog import views
from users.views import register_user
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page),
    path('create_article/', views.create_article),
    path('news/', views.news_page, name='news'),
    path('articles/', views.articles),
    path(r'articles/delete/<int:id>', views.delete),
    path('register/', register_user, name='register'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''path('admin/', views.admin.site.urls),'''
