# Generated by Django 4.1.1 on 2022-09-19 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_articles_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='img_article',
            field=models.ImageField(blank=True, null=True, upload_to='imgarticles/'),
        ),
    ]
