from django.contrib import admin
from .models import Article,Category,IPAddress
from django.contrib import messages
from django.utils.translation import ngettext

#------Actions----------

@admin.action(description='انتشار مقالات انتخاب شده')
def make_published(self, request, queryset):
	updated = queryset.update(status='p')
	self.message_user(request, ngettext(
		'%d مقاله با موفقیت منتشر شد..',
		'%d مقاله با موفقیت منتشر شدند.',
		updated,
	) % updated, messages.SUCCESS)

@admin.action(description='پیشنویس مقالات انتخاب شده')
def make_draft(self, request, queryset):
	updated = queryset.update(status='d')
	self.message_user(request, ngettext(
		'%d مقاله با موفقیت  پیش نویس شد..',
		'%d مقاله با موفقیت  پیش نویس شدند.',
		updated,
	) % updated, messages.SUCCESS)



#-------Admin class------- 

class ArticleAdmin(admin.ModelAdmin):
	list_display=('title','thumbnail_tag','slug','author','jpublish','is_special','category_to_str','status')
	list_filter=('publish','status','author')
	prepopulated_fields={'slug':('title',)}
	ordering=['status','publish']
	actions=[make_published,make_draft]



admin.site.register(Article,ArticleAdmin)
admin.site.register(IPAddress)

class CategoryAdmin(admin.ModelAdmin):
	list_display=('position','title','slug','status')
	list_filter=(['status'])
	prepopulated_fields={'slug':('title',)}

admin.site.register(Category,CategoryAdmin)


