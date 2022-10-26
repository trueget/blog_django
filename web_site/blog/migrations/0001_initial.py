# Generated by Django 4.1.1 on 2022-10-25 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_article', models.CharField(max_length=200)),
                ('img_article', models.ImageField(blank=True, null=True, upload_to='imgarticles/')),
                ('text_article', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
