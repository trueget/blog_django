from django.apps import AppConfig


class UserPageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_page'
    verbose_name: str = 'Страница пользователя'
