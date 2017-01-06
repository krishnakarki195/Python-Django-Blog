from django.contrib import admin
from . models import Blog, BlogType
from django import forms
from ckeditor.widgets import CKEditorWidget

class BlogAdminForm(forms.ModelForm):
	blog_content = forms.CharField(widget=CKEditorWidget())

	class Meta:
		model = Blog
		fields = [
			'blog_type',
			'blog_author',
			'blog_header',
			'blog_content',
			'blog_added_date',
			'blog_updated_date'
		]


class BlogAdmin(admin.ModelAdmin):
	form = BlogAdminForm



class BlogTypeAdmin(admin.ModelAdmin):
	fields = ['name']



admin.site.register(Blog,BlogAdmin)
admin.site.register(BlogType,BlogTypeAdmin)