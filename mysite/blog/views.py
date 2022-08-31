from django.shortcuts import render,get_object_or_404
from .models import Article,Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView,DetailView



class ArticleList(ListView):
	queryset=Article.objects.published()
	paginate_by=2


class ArticleDetail(DetailView):

	def get_object(self):
		slug=self.kwargs.get('slug')
		return get_object_or_404(Article.objects.published(),slug=slug)

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



