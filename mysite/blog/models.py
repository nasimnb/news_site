from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter
# Create your models here.


class Category(models.Model):

	class Meta:
		verbose_name="دسته بندی"
		verbose_name_plural="دسته بندی ها"
		ordering=['position']

	title=models.CharField(max_length=200,verbose_name="عنوان")
	slug=models.SlugField(max_length=100,unique=True,verbose_name="آدرس")
	status=models.BooleanField(max_length=1,verbose_name="آیا نمایش داده شود؟")
	position=models.IntegerField(verbose_name='پوزیشن')
	
	def __str__(self):
		return self.title



class Article(models.Model):

	class Meta:
		verbose_name='مقاله'
		verbose_name_plural="مقالات"

	STATUS_CHOICES=(
		('d','پیش نویس'),
		('p','منتشر شده')
		)
	title=models.CharField(max_length=200,verbose_name="عنوان")
	slug=models.SlugField(max_length=100,unique=True,verbose_name="آدرس")
	category=models.ManyToManyField(Category,verbose_name="دسته بندی",related_name='articles')
	description=models.TextField(verbose_name="محتوا")
	thumbnail=models.ImageField(upload_to='images',verbose_name="عکس")
	publish=models.DateTimeField(default=timezone.now,verbose_name="زمان انتشار")
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	status=models.CharField(max_length=1,choices=STATUS_CHOICES,verbose_name="وضعیت")

	def __str__(self):
		return self.title

	def jpublish(self):
		return jalali_converter(self.publish)
	jpublish.short_description='زمان انتشار'

	def category_publish(self):
		return self.category.filter(status=True)

