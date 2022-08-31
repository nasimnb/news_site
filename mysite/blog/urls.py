from django.urls import path
from .views import ArticleList,ArticleDetail,Categorylist

app_name="blog"
urlpatterns = [
	path('',ArticleList.as_view(),name='home'),
	path('page/<int:page>', ArticleList.as_view(), name='home'),
	path('article/<slug:slug>', ArticleDetail.as_view(), name='detail'),
	path('category/<slug:slug>', Categorylist.as_view(), name='category'),
	path('category/<slug:slug>/page/<int:page>',Categorylist.as_view(),name='category'),
]
