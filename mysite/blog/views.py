from django.shortcuts import render,get_object_or_404
from .models import Article,Category
from account.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView,DetailView
from account.mixins import AuthorAccessMixin


class ArticleList(ListView):
	queryset=Article.objects.published()
	paginate_by=2


class ArticleDetail(DetailView):
	def get_object(self):
		slug = self.kwargs.get('slug')
		article = get_object_or_404(Article.objects.published(), slug=slug)

		ip_address = self.request.user.ip_address
		if ip_address not in article.hits.all():
			article.hits.add(ip_address)

		return article

class Categorylist(ListView):
	paginate_by=2
	template_name='blog/category_list.html'

	def get_queryset(self):
		global category
		slug=self.kwargs.get('slug')
		category=get_object_or_404(Category.objects.active(),slug=slug)
		return category.articles.published()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['category'] = category
		return context


class Authorlist(ListView):
	paginate_by=2
	template_name='blog/author_list.html'

	def get_queryset(self):
		global author
		username=self.kwargs.get('username')
		author=get_object_or_404(User,username=username)
		return author.articles.published()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['author'] = author
		return context


class ArticlePreview(AuthorAccessMixin,DetailView):
	def get_object(self):
		pk=self.kwargs.get('pk')
		return get_object_or_404(Article,pk=pk)
