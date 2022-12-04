# Generated by Django 4.1 on 2022-12-04 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_article_hits'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleHit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', through='blog.ArticleHit', to='blog.ipaddress', verbose_name='بازدیدها'),
        ),
        migrations.AddField(
            model_name='articlehit',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article'),
        ),
        migrations.AddField(
            model_name='articlehit',
            name='ip_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.ipaddress'),
        ),
    ]
