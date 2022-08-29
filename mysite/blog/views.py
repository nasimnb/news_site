from django.shortcuts import render,get_object_or_404
from .models import Article,Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def Home(request):
	article_list=Article.objects.published()
	page = request.GET.get('page',1)

	paginator = Paginator(article_list,2)
	try:
		article = paginator.page(page)
	except PageNotAnInteger:
		article = paginator.page(1)
	except EmptyPage:
		article = paginator.page(paginator.num_pages)

	context={
	"articles":article,
	}
	return render(request,'blog/home.html',context)


def detail(request,slug):
	context={
	"article":get_object_or_404(Article.objects.published(),slug=slug)
	}
	return render(request,'blog/detail.html',context)

def category(request,slug):
	context={
	"category":get_object_or_404(Category,slug=slug,status=True)
	}
	return render(request,'blog/category.html',context)	

