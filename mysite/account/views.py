from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Article
from django.views.generic import ListView



class ArticleList(LoginRequiredMixin,ListView):
	queryset=Article.objects.all()
	template_name="registration/home.html"

