from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
	is_author=models.BooleanField(default=False,verbose_name='وضعیت  نویسنده')
	is_special=models.DateTimeField(default=timezone.now,verbose_name="کاربر ویژه تا")
	
	def is_special_user(self):
		if self.special_user > timezone.now():
			return True
		else:
			return False
