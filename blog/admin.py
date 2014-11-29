from django.contrib import admin
from blog.models import Category, Label, Post

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}

class LabelAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}

class PostAdmin(admin.ModelAdmin):
	date_hirearchy = 'pub_date'
	list_display = ('title', 'pub_date')
	fieldsets = [
		(None, { 'fields': [ 'title', 'slug', 'lead', 'content', 'category', 'labels' ] }),
		('Publication', { 'fields': [ 'pub_date', 'published' ] })
	]
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(Post, PostAdmin)
