from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Article
from django.urls import reverse_lazy
from .models import User
from django.views.generic import (
	ListView,
	CreateView,
	UpdateView,
	DeleteView
	)
from .mixins import (
	FieldsMixin,
	FormValidMixin,
	AuthorAccessMixin,
	SuperUserAccessMixin
	)


class ArticleList(LoginRequiredMixin,ListView):
	def get_queryset(self):
		if self.request.user.is_superuser:
			return	Article.objects.all()
		else:
			return	Article.objects.filter(author=self.request.user)
	template_name="registration/home.html"

class ArticleCreate(FieldsMixin,FormValidMixin,CreateView):
	model=Article
	fields=["author","title","slug","category","description","thumbnail","publish","status"]
	template_name="registration/article_create_update.html"


class ArticleUpdate(AuthorAccessMixin,FieldsMixin,FormValidMixin,UpdateView):
	model=Article
	template_name="registration/article_create_update.html"


class ArticleDelete(SuperUserAccessMixin,DeleteView):
	model = Article
	success_url = reverse_lazy('account:home')
	template_name="registration/article_confirm_delete.html"


class Profile(UpdateView):
	model=User
	template_name="registration/profile.html"
	fields=['username','email','first_name','last_name','special_user','is_author']
	success_url=reverse_lazy("account:profile")
	def get_object(self):
		return User.objects.get(pk=self.request.user.pk)
		