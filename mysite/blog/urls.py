from django.urls import path
from .views import Home,detail,category

app_name="blog"
urlpatterns = [
	path('', Home, name='home'),
	path('article/<slug:slug>', detail, name='detail'),
	path('category/<slug:slug>', category, name='category'),
]
