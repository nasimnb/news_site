from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Article
from django.views.generic import ListView,CreateView,UpdateView
from .mixins import Fieldmixins,FormValidMixin,AuthorAccessMixin


class ArticleList(LoginRequiredMixin,ListView):
	def get_queryset(self):
		if self.request.user.is_superuser:
			return	Article.objects.all()
		else:
			return	Article.objects.filter(author=self.request.user)
	template_name="registration/home.html"

class ArticleCreate(AuthorAccessMixin,Fieldmixins,FormValidMixin,CreateView):
	model=Article
	fields=["author","title","slug","category","description","thumbnail","publish","status"]
	template_name="registration/article_create_update.html"


class ArticleUpdate(AuthorAccessMixin,Fieldmixins,FormValidMixin,UpdateView):
	model=Article
	template_name="registration/article_create_update.html"