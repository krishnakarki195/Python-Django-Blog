from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField

class BlogType(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return str(self.name)


class Blog(models.Model):
	blog_author = models.ForeignKey(
		User,
		on_delete = models.CASCADE,
		related_name='blogs',
		default=1
	)
	blog_header = models.CharField(max_length=500)
	blog_content = RichTextField()
	blog_added_date = models.DateTimeField(auto_now_add=False)
	blog_updated_date = models.DateTimeField(auto_now_add=False)

	blog_type = models.ForeignKey(
		BlogType,
		on_delete=models.CASCADE,
		related_name='blogtyps',
		blank = True
	)

	def __str__(self):
		return str(self.blog_header)

	def get_absolute_url(self):
		return reverse('blog:blog-detail',kwargs={'pk': self.pk})

	def get_update_url(self):
		return reverse('blog:blog-update',kwargs={'pk': self.pk})

	def get_delete_url(self):
		return reverse('blog:blog-delete',kwargs={'pk': self.pk})