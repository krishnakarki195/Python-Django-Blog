from django import forms
from . models import Blog, BlogType
from django.contrib.auth.models import User


class BlogForm(forms.ModelForm):
	blog_type = forms.ChoiceField(widget = forms.Select(), choices=[BlogType.objects.all()])

	class Meta:
		model = Blog
		fields = [
			'blog_header',
			'blog_content',
			'blog_added_date',
			'blog_updated_date',
			'blog_type'
		]


class SignupForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password']


class LoginForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'password']