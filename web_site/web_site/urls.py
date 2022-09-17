from django.contrib import admin
from django.urls import path
from blog.views import index_page, create_article, news_page, articles
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('create_article/', create_article),
    path('news/', news_page),
    path('articles/', articles),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
