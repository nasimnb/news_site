from django.urls import path
from .views import Home,detail

app_name="blog"
urlpatterns = [
	path('', Home, name='home'),
	path('article/<slug:slug>', detail, name='detail'),
]
