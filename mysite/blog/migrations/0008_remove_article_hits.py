# Generated by Django 4.1 on 2022-12-04 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_ipaddress_article_hits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='hits',
        ),
    ]
