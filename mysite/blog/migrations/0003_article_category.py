# Generated by Django 4.1 on 2022-08-26 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_alter_article_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(related_name='article', to='blog.category', verbose_name='دسته بندی'),
        ),
    ]