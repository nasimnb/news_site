from django.shortcuts import render
from .models import Article


def Home(request):
	context={
	"articles":Article.objects.filter(status='p')
	}
	return render(request,'blog/home.html',context)


def detail(request,slug):
	context={
	"article":Article.objects.get(slug=slug)
	}
	return render(request,'blog/detail.html',context)

