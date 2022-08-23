from django.urls import path
from .views import Home

app_name="blog"
urlpatterns = [
	path('', Home, name='home'),
]
