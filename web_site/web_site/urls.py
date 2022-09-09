from django.contrib import admin
from django.urls import path
from blog.views import index_page, publish_page, news_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('publish/', publish_page),
    path('news/', news_page),
]
