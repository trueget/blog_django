## blog_django
### Первый большой проект на Django
[ссылка на готовый продукт](https://trueget.pythonanywhere.com)

### Структура проекта
'''
.
├── web_site
    ├── blog
    ├── user_page
    ├── users
    ├── web_site
    ├── db_blog.sqlite3
    └── manage.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
'''


### Описание приложения

В блоге присутствует регистрация пользователя, без авторизации функционал будел слегка ограничен.
Страницы регистрации, авторизации и подтверждения регистрации:
![страница регистрации](./img_from_project/register.png)
![страница подтверждения регистрации](./img_from_project/activation.png)
![страница авторизации](./img_from_project/login.png)

Без авторизации функционал ограничен: вы можете только просматривать статью, просматривать страницу авторов, доступен поиск по ключевым словам и доступен выбор раздела статтей, доступна функция поиска по ключевому слову:
![страница пользователя без авторизации](./img_from_project/another_user_page_not_login.png)
![поиск статьи по ключевому слову](./img_from_project/search.png)
![выбор раздела статьи](./img_from_project/articles_section.png)
![share](./img_from_project/link_share.png)

После авторизации у вас появляется возможность: опубликовать статью, комментировать, ставить лайк, изменять свой профиль:
![главная страница с авторизованым пользователем](./img_from_project/main_page.png)
![страница чужого пользователя](./img_from_project/another_user_page.png)
![изменить свой профиль](./img_from_project/change_profile.png)
![все авторы](./img_from_project/authors.png)
![страница одной публикации: информация о статье](./img_from_project/one_article_page_top.png)
![страница одной публикации: лайки, просмотры и комментарии](./img_from_project/another_article_page_bot.png)

<br>
<h3>Для запуска приложения:</h3>
<ul>
    <li>скачайте либо клонируйте репозиторий с проектом</li>
    <li>установите зависимости через requirements</li>
    <li>создайтк бд в папке web_site где находится файл запуска manage.py</li>
    <li>сделайте миграцию моделей</li>
    <li>создайте суперюзера</li>
    <li>в файле setting главного приложения проекта, вам необходимо установить ваши значения в SECRET_KEY, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD. так как мои значения храняться в переменных окружения.</li>
    <li>запустить приложение</li>
</ul>
