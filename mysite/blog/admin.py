from django.contrib import admin
from .models import Article,Category


class ArticleAdmin(admin.ModelAdmin):
	list_display=('title','slug','jpublish','category_to_str','status')
	list_filter=('publish','status')
	prepopulated_fields={'slug':('title',)}
	ordering=['status','publish']
	def category_to_str(self,obj):
		return "، ".join([category.title for category in obj.category.all()])
	category_to_str.short_description="دسته بندی"


admin.site.register(Article,ArticleAdmin)

class CategoryAdmin(admin.ModelAdmin):
	list_display=('position','title','slug','status')
	list_filter=(['status'])
	prepopulated_fields={'slug':('title',)}





admin.site.register(Category,CategoryAdmin)
